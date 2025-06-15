from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    role = models.CharField(max_length=20, choices=[('veterinarian', 'Veterinarian'), ('owner', 'Owner')])

    def __str__(self):
        return f"{self.email} ({self.role})"
