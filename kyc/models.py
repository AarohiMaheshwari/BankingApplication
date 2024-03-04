# models.py

from django.db import models
from django.contrib.auth.models import User

class KYCDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # account_number = models.CharField(max_length=100)  # New field for account number
    document = models.FileField(upload_to='kyc_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s KYC Document"
