from .models import VetSubscription
from ..base_classes.base_repository import BaseRepository


class VetSubscriptionRepository(BaseRepository):
    model = VetSubscription
