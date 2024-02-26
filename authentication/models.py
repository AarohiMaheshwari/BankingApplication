# # models.py

from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class BankAccount(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Bank Account of {self.owner}"

    def deposit(self, amount):
        self.balance += amount
        self.save()
        Transaction.objects.create(account=self, transaction_type='Deposit', amount=amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            Transaction.objects.create(account=self, transaction_type='Withdrawal', amount=amount)
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
class Transaction(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} for {self.account}"
    