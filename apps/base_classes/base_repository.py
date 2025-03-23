from abc import ABC
from django.db import models

class BaseRepository(ABC):
    model: models.Model

    @classmethod
    def get_all(cls):
        return cls.model.objects.all()

    @classmethod
    def get_by_id(cls, obj_id):
        return cls.model.objects.filter(id=obj_id).first()

    @classmethod
    def create(cls, data):
        return cls.model.objects.create(**data)

    @classmethod
    def update(cls, obj_id, data):
        obj = cls.model.objects.filter(id=obj_id).first()
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        return None

    @classmethod
    def delete(cls, obj_id):
        return cls.model.objects.filter(id=obj_id).delete()