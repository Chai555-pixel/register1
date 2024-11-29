# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    # The RegisterForm inherits from UserCreationForm to handle user registration
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
