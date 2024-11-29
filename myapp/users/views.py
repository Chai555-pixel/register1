# users/views.py
# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            user = form.save()
            # Log in the user automatically after registration
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('posts')  # Redirect to the posts page or dashboard
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def sign_in(request):
    """
    Handle the login process.
    If the user is already authenticated, redirect to the posts page.
    If not, authenticate and log the user in upon valid credentials.
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('posts')  # Redirect to posts if already logged in
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('posts')  # Redirect to posts page after successful login
        messages.error(request, 'Invalid username or password')
        return render(request, 'users/login.html', {'form': form})

def sign_out(request):
    """
    Log out the user and redirect to the login page.
    """
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Redirect to the login page after logout


