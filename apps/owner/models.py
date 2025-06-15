from django.db import models
from apps.accounts.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    CNP = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    number_of_animals = models.IntegerField(default=0)

    class Meta:
        db_table = "owner"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
