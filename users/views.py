from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    return render(request, 'splash/index.html')

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
