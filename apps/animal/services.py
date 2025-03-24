from .repositories import AnimalRepository

class AnimalService:
    @staticmethod
    def list_animals():
        return AnimalRepository.get_all()

    @staticmethod
    def create_animal(data):
        return AnimalRepository.create(data)

    @staticmethod
    def delete_animal(animals_id):
        return AnimalRepository.delete(animals_id)
