from .repositories import OwnerRepository

class OwnerService:
    @staticmethod
    def list_owners():
        return OwnerRepository.get_all_owners()

    @staticmethod
    def create_owner(data):
        return OwnerRepository.create_owner(data)

    @staticmethod
    def delete_owner(owner_id):
        return OwnerRepository.delete_owner(owner_id)
