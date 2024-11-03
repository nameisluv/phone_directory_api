from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)  # unique per user
    created_at = models.DateTimeField(auto_now_add=True)

class SpamReport(models.Model):
    contact_number = models.CharField(max_length=15)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('contact_number', 'reported_by')
