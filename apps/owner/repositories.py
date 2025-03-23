from .models import Owner
from ..base_classes.base_repository import BaseRepository


class OwnerRepository(BaseRepository):
    model = Owner
