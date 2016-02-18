from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from .forms import LoginForm

# Create your views here.

def index(request):
    registrationForm = RegistrationForm()
    loginForm = LoginForm()
    return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm})
