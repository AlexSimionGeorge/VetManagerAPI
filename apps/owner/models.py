from django.db import models

class Owner(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    CNP = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    number_of_animals = models.IntegerField()
    password = models.CharField(max_length=255)

    class Meta:
        db_table = "owner"

    def __str__(self):
        return self.name
