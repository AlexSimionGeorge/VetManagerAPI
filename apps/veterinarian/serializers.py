from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
import re

User = get_user_model()

class VeterinarianSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField(required=True, allow_blank=False)
    last_name = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(write_only=True, min_length=8)

    phone_number = serializers.CharField()

    cabinet_address = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'phone_number', 'cabinet_address', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_phone_number(self, value):
        # Regex for phone: digits, optional leading +, length 7-15
        phone_regex = re.compile(r'^\+?\d{7,15}$')
        if not phone_regex.match(value):
            raise serializers.ValidationError(
                "Phone number must be 7-15 digits and can start with a +."
            )
        return value

    def validate_cabinet_address(self, value):
        # Only letters, numbers, and these symbols: [.,/:;-\ ]
        addr_regex = re.compile(r'^[a-zA-Z0-9\[\].,/:;\\\- ]+$')
        if not addr_regex.match(value):
            raise serializers.ValidationError(
                "Cabinet address can only contain letters, numbers, and [.,/:;\\-]"
            )
        return value

    def create(self, validated_data):
        # Use create_user to handle password hashing
        user = User.objects.create_user(**validated_data)
        return user
