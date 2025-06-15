from rest_framework import serializers
from apps.veterinarian.models import Veterinarian
from apps.accounts.serializers import UserSerializer

class VeterinarianSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    phone_number = serializers.CharField()
    cabinet_address = serializers.CharField()

    class Meta:
        model = Veterinarian
        fields = ['user', 'phone_number', 'cabinet_address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'veterinarian'
        user = UserSerializer().create(user_data)
        vet = Veterinarian.objects.create(user=user, **validated_data)
        return vet

