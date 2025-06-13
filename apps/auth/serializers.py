from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username_or_email'

    username_or_email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        login = attrs.get('username_or_email')
        password = attrs.get('password')

        user = authenticate(username=login, password=password)
        if not user:
            # Try email login
            from django.contrib.auth import get_user_model
            User = get_user_model()
            try:
                user_obj = User.objects.get(email=login)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass

        if not user:
            raise serializers.ValidationError('Invalid credentials')

        refresh = self.get_token(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
