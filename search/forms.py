# forms.py

from django import forms

class SearchForm(forms.Form):
    bank_account_id = forms.CharField(label='Bank Account ID')
