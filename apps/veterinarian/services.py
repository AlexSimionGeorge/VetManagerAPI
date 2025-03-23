from .repositories import VeterinarianRepository

class VeterinarianService:
    @staticmethod
    def list_owners():
        return VeterinarianRepository.get_all()

    @staticmethod
    def create_owner(data):
        return VeterinarianRepository.create(data)

    @staticmethod
    def delete_owner(owner_id):
        return VeterinarianRepository.delete(owner_id)
