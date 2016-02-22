from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from social_todo.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

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
                registrationForm = RegistrationForm()
                loginForm = LoginForm()
                return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Invalid password'})

        else:
            registrationForm = RegistrationForm()
            loginForm = LoginForm()
            return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Invalid password'})

    else:
        registrationForm = RegistrationForm()
        loginForm = LoginForm()
        return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Invalid email address'})

# handles registering a user
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if len(data['fl_name']) > 50:
                registrationForm = RegistrationForm()
                loginForm = LoginForm()
                return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Name too long'})

            if len(data['password']) > 50:
                registrationForm = RegistrationForm()
                loginForm = LoginForm()
                return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Password too long'})

            if data['password'] == data['password_confirmation']:
                if User.objects.filter(username=data['email']).exists():
                    registrationForm = RegistrationForm()
                    loginForm = LoginForm()
                    return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Account with this email already exists!'})
                else:
                    user = User.objects.create_user(data['email'], '', data['password'], first_name=data['fl_name'])
                    user = authenticate(username=data['email'], password=data['password'])
                    auth_login(request, user)
                    return HttpResponseRedirect('/')
            else:
                registrationForm = RegistrationForm()
                loginForm = LoginForm()
                return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Passwords do not match'})

        else:
            registrationForm = RegistrationForm()
            loginForm = LoginForm()
            return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Fill out all fields'})

    return HttpResponseRedirect('/')

# logs users out
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
