from django.db import models
from apps.accounts.models import User

class Veterinarian(models.Model):
    class Meta:
        db_table = "veterinarian"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    cabinet_address = models.CharField(max_length=255)
