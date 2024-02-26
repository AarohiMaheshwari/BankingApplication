

# Register your models here.
# admin.py

from django.contrib import admin
from .models import BankAccount, Transaction

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ['owner', 'balance']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'transaction_type', 'amount', 'timestamp']

admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
