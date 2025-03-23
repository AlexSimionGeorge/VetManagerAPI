from .repositories import OwnerRepository

class OwnerService:
    @staticmethod
    def list_owners():
        return OwnerRepository.get_all()

    @staticmethod
    def create_owner(data):
        return OwnerRepository.create(data)

    @staticmethod
    def delete_owner(owner_id):
        return OwnerRepository.delete(owner_id)
