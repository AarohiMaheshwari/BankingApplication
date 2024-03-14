# urls.py

from django.urls import path
from . import views
from .views import edit_profile

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    # Other URL patterns for your application
]
