from django.contrib.auth.models import AbstractUser
from django.db import models

class Veterinarian(AbstractUser):
    phone_number = models.CharField(max_length=20)
    cabinet_address = models.CharField(max_length=255)

    class Meta:
        db_table = "veterinarian"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
