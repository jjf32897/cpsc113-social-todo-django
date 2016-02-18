from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("you fucked up")

    else:
        return HttpResponse("account doesn't exist")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(data['name'], data['email'], data['password'])
            return HttpResponseRedirect('/')

    else:
        registrationForm = RegistrationForm()
        loginForm = LoginForm()

    return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm})

def logout(request):
    auth_logout(request)
    registrationForm = RegistrationForm()
    loginForm = LoginForm()

    return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm})
