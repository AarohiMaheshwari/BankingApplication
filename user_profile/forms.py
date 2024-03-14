# forms.py

from django import forms
from django.contrib.auth.models import User

class ProfilePictureForm(forms.Form):
    profile_picture = forms.ImageField(label='Profile Picture', required=False)


    
