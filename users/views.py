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
            return HttpResponse("Error")

    else:
        registrationForm = RegistrationForm()
        loginForm = LoginForm()
        return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Invalid email address'})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['password'] == data['password_confirmation']:
                user = User.objects.create_user(data['email'], '', data['password'], first_name=data['name'])
                user = authenticate(username=data['email'], password=data['password'])
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Passwords do not match')
        else:
            registrationForm = RegistrationForm()
            loginForm = LoginForm()
            return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Name too short'})

    return HttpResponseRedirect('/')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
