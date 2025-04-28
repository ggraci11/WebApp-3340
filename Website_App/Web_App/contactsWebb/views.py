from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request,"home.html",{})

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)

        return redirect('home')  # redirect to avoid re-submitting the form

    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')  # redirect to home or dashboard
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')