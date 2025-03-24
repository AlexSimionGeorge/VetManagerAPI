from .models import Animal
from ..base_classes.base_repository import BaseRepository

class AnimalRepository(BaseRepository):
    model = Animal
