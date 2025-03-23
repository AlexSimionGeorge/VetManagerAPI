from .models import Veterinarian
from ..base_classes.base_repository import BaseRepository

class VeterinarianRepository(BaseRepository):
    model = Veterinarian
