from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Task

def index(request):
    return render(request, 'index.html')

def createTask(request):
    all_users = User.objects.all()
    context = {
        'all_users': all_users
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        deadline = request.POST.get('deadline')
        description = request.POST.get('description')
        owner = request.POST.get('owner')
        supervisor = request.POST.get('supervisor')
        state = request.POST.get('state')
        print(state)
        
        task = Task(title=title, deadline=deadline, description=description, owner=User.objects.get(username=owner), supervisor=User.objects.get(username=supervisor), state=state)
        task.save()
        return redirect(index)
    return render(request, 'createTask.html', context)

def taskAssigned(request):
    task_assigned = Task.objects.filter(owner=request.user)
    print(task_assigned)
    context = {
        "task_assigned": task_assigned
    }
    return render(request, 'tasksAssigned.html', context)

def taskEdit(request, id):
    task = Task.objects.get(id=id)
    all_users = User.objects.all()
    context = {
        "task": task,
        'all_users': all_users
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        deadline = request.POST.get('deadline')
        description = request.POST.get('description')
        owner = request.POST.get('owner')
        supervisor = request.POST.get('supervisor')
        state = request.POST.get('state')
        print(state)
        
        task = Task(title=title, deadline=deadline, description=description, owner=User.objects.get(username=owner), supervisor=User.objects.get(username=supervisor), state=state)
        task.save()
    return render(request, 'editTask.html', context)