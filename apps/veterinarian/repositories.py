from .models import Veterinarian

class VeterinarianRepository:
    @staticmethod
    def get_all_veterinarians():
        return Veterinarian.objects.all()

    @staticmethod
    def get_veterinarian_by_id(veterinarian_id):
        return Veterinarian.objects.filter(id=veterinarian_id).first()

    @staticmethod
    def create_veterinarian(data):
        return Veterinarian.objects.create(**data)

    @staticmethod
    def update_veterinarian(veterinarian_id, data):
        veterinarian = Veterinarian.objects.filter(id=veterinarian_id).first()
        if veterinarian:
            for key, value in data.items():
                setattr(veterinarian, key, value)
            veterinarian.save()
            return veterinarian
        return None

    @staticmethod
    def delete_veterinarian(veterinarian_id):
        return Veterinarian.objects.filter(id=veterinarian_id).delete()
