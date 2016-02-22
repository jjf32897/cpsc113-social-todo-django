from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tasks.models import Task
from social_todo.forms import NewTaskForm
from django.contrib.auth.models import User
from django.core.mail import send_mail

# handles task creation
def create(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # makes a task with the submitted information and the current user
            task = Task(owner=request.user, title=data['title'], description=data['description'])
            task.save()

            # adds collaborators 1, 2 and 3 by finding the user associated with the submitted email
            for x in range(1, 4):
                if User.objects.filter(username=data['collaborator' + str(x)]).exists():
                    task.collaborators.add(User.objects.get(username=data['collaborator' + str(x)]))

            task.save()

    return HttpResponseRedirect('/')

# deletes a task
def delete(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.delete()

    return HttpResponseRedirect('/')

# toggles the completion of a task
def toggle(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        if task.isComplete == True:
            task.isComplete = False
        else:
            # for x in range(1, 4):
            # send_mail('Your task has been complete!', 'Your task ' + task.title + ' has been completed!', 'dollaborate@gmail.com', [task.collaborators[x].email], fail_silently=False)
            task.isComplete = True

        task.save()

    return HttpResponseRedirect('/')
