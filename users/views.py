from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from social_todo.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse

# function to render the homepage with errors
def returnErrors(request, errors):
    registrationForm = RegistrationForm()
    loginForm = LoginForm()
    return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': errors})

# handles logging a user in
def login(request):
    email = request.POST['email']
    password = request.POST['password']
    if User.objects.filter(username=email).exists():
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return returnErrors(request, 'Invalid password')

        else:
            return returnErrors(request, 'Invalid password')

    else:
        return returnErrors(request, 'Invalid email address')

# handles registering a user
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if len(data['fl_name']) > 50:
                return returnErrors(request, 'Name too long')

            if len(data['password']) > 50:
                return returnErrors(request, 'Password too long')

            if data['password'] == data['password_confirmation']:
                if User.objects.filter(username=data['email']).exists():
                    return returnErrors(request, 'Account with this email already exists!')
                else:
                    user = User.objects.create_user(data['email'], '', data['password'], first_name=data['fl_name'])
                    user = authenticate(username=data['email'], password=data['password'])
                    auth_login(request, user)
                    return HttpResponseRedirect('/')
            else:
                return returnErrors(request, 'Passwords do not match')

        else:
            return returnErrors(request, 'Fill out all fields')

    return HttpResponseRedirect('/')

# logs users out
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
