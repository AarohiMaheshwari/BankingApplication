# forms.py

# forms.py

from django import forms
from .models import CardApplication

class CardApplicationForm(forms.ModelForm):
    class Meta:
        model = CardApplication
        fields = ['card_type', 'issue_date', 'expiry_date']
