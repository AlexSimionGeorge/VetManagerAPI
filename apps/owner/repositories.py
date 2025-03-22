from .models import Owner

class OwnerRepository:
    @staticmethod
    def get_all_owners():
        return Owner.objects.all()

    @staticmethod
    def get_owner_by_id(owner_id):
        return Owner.objects.filter(id=owner_id).first()

    @staticmethod
    def create_owner(data):
        return Owner.objects.create(**data)

    @staticmethod
    def delete_owner(owner_id):
        return Owner.objects.filter(id=owner_id).delete()
