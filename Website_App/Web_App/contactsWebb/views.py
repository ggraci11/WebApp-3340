from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def home_view(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        due_date = request.POST.get('due_date', None)

        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                description=description,
                due_date=due_date if due_date else None
            )
        return redirect('home')

    tasks = Task.objects.filter(user=request.user)

    return render(request, 'home.html', {'tasks': tasks})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('home')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title', '').strip()
        task.description = request.POST.get('description', '').strip()
        due_date = request.POST.get('due_date', None)
        task.due_date = due_date if due_date else None
        task.save()
        return redirect('home')

    return render(request, 'edit_task.html', {'task': task})


def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        role = request.POST['role']  # You can save this separately if needed

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        # Create user
        user = User.objects.create_user(username=username, password=password1)
        user.save()

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')  # Redirect back to login after registration

    return render(request, 'register.html')