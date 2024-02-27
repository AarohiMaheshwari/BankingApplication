# forms.py

from django import forms
from .models import KYCDocument

class KYCDocumentForm(forms.ModelForm):
    class Meta:
        model = KYCDocument
        fields = ['account_number', 'document']
