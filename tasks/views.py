from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tasks.models import Task
from .forms import NewTaskForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def create(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task(owner=request.user, title=data['title'], description=data['description'])
            task.save()
            task.collaborators.add(data['collaborator1'])
            task.collaborators.add(data['collaborator2'])
            task.collaborators.add(data['collaborator3'])
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
