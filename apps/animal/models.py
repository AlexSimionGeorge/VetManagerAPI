from django.db import models
from apps.owner.models import Owner

class Animal(models.Model):
    name = models.CharField(max_length=255)

    sex = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ]) #(value for db, prompt ui)

    castrated = models.BooleanField()
    birth_date = models.DateField()
    has_microchip = models.BooleanField()
    microchip_id = models.CharField(max_length=255)

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='animals')

    class Meta:
        db_table = "animal"

    def __str__(self):
        return self.name
