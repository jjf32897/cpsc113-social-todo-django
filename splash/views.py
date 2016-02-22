from django.shortcuts import render
from django.http import HttpResponse
from social_todo.forms import RegistrationForm, LoginForm, NewTaskForm
from django.contrib.auth.models import User
from tasks.models import Task
from django.db.models import Q

# Create your views here.

# renders the task dashboard and the home page
def index(request):
    if request.user.is_authenticated():
        newTaskForm = NewTaskForm()

        # finds the tasks where the current user is the owner or a collaborator
        tasks = Task.objects.filter(Q(owner=request.user) | Q(collaborators=request.user))
        return render(request, 'splash/index.html', {'user': request.user, 'new_task': newTaskForm, 'tasks': tasks})

    else:
        registrationForm = RegistrationForm()
        loginForm = LoginForm()
        return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm})
