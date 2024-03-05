# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    # Other URL patterns for your application
]
