# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.sign_in, name='login'),  # Login page
    path('logout/', views.sign_out, name='logout'),  # Logout page
    path('register/', views.sign_up, name='register'),  # Registration page
]
