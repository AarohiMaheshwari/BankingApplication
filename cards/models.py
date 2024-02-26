# models.py

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class CardType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CardApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_type = models.ForeignKey(CardType, on_delete=models.CASCADE)
    issue_date = models.DateField(default=datetime.now)
    expiry_date = models.DateField(default=datetime.now())
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.card_type.name} Application"
