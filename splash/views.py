from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.user.is_authenticated():
        return render(request, 'splash/index.html', {'user': request.user})

    else:
        registrationForm = RegistrationForm()
        loginForm = LoginForm()
        return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm})
