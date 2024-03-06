# forms.py

from django import forms

class ProfilePictureForm(forms.Form):
    profile_picture = forms.ImageField(label='Profile Picture', required=False)
