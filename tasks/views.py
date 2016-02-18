from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def add(request):
    return HttpResponse("You tried to add a new task, right?")

def delete(request):
    return HttpResponse("You tried to delete a task, right?")
