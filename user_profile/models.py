# models.py

from django.db import models
from django.contrib.auth.models import User

class ProfilePicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
