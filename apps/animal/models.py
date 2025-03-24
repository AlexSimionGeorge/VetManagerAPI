from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    castrated = models.BooleanField()
    birth_date = models.DateField()
    has_microchip = models.BooleanField()
    microchip_id = models.CharField(max_length=255)


    class Meta:
        db_table = "animal"

    def __str__(self):
        return self.name
