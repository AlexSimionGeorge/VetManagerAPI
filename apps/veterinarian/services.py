from .repositories import VeterinarianRepository

class VeterinarianService:
    @staticmethod
    def list_owners():
        return VeterinarianRepository.get_all_veterinarians()

    @staticmethod
    def create_owner(data):
        return VeterinarianRepository.create_veterinarian(data)

    @staticmethod
    def delete_owner(owner_id):
        return VeterinarianRepository.delete_veterinarian(owner_id)
