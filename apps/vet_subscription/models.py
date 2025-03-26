from django.db import models

from apps.owner.models import Owner
from apps.veterinarian.models import Veterinarian


class VetSubscription(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    vet = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "vet_subscription"

    def __str__(self):
        return "Owner:" + self.owner.name + " | Vet:" + self.vet.name
