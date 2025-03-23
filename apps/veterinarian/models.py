from django.db import models

class Veterinarian(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cabinet_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = "veterinarian"

    def __str__(self):
        return self.name
