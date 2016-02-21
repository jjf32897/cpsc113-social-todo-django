from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tasks.models import Task
from social_todo.forms import NewTaskForm
from django.contrib.auth.models import User

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task(owner=request.user, title=data['title'], description=data['description'])
            task.save()

            for x in range(1, 4):
                if User.objects.filter(username=data['collaborator' + str(x)]).exists():
                    task.collaborators.add(User.objects.get(username=data['collaborator' + str(x)]))

            task.save()

    return HttpResponseRedirect('/')

def delete(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.delete()

    return HttpResponseRedirect('/')

def toggle(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        if task.isComplete == True:
            task.isComplete = False
        else:
            task.isComplete = True

        task.save()

    return HttpResponseRedirect('/')
