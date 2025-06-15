from rest_framework import serializers
from apps.accounts.serializers import UserSerializer
from .models import Owner

class OwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    city = serializers.CharField()
    street = serializers.CharField()
    number = serializers.CharField()
    county = serializers.CharField()
    CNP = serializers.CharField()
    phone_number = serializers.CharField()
    number_of_animals = serializers.IntegerField(read_only=True)

    class Meta:
        model = Owner
        fields = ['user', 'city', 'street', 'number', 'county', 'CNP', 'phone_number', 'number_of_animals']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'owner'  # Force owner role
        user = UserSerializer().create(user_data)
        owner = Owner.objects.create(user=user, **validated_data)
        return owner
