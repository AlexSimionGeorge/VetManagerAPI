# Django REST Framework
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

# Google Auth
from google.oauth2 import id_token
from google.auth.transport import requests
import os
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

# Local Apps
from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer
from apps.owner.serializers import OwnerSerializer
from apps.veterinarian.serializers import VeterinarianSerializer
from .serializers import LoginSerializer


class VeterinarianRegisterView(generics.CreateAPIView):
    serializer_class = VeterinarianSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

class GoogleLoginView(APIView):
    def post(self, request):
        token = request.data.get("google_token")
        if not token:
            return Response({"detail": "Missing ID token"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

            # ID token is valid. Get user info
            email = idinfo.get("email")
            first_name = idinfo.get("given_name", "")
            last_name = idinfo.get("family_name", "")
            picture = idinfo.get("picture", "")
            username = email.split("@")[0]

            if not email:
                return Response({"detail": "Email not provided by Google."}, status=status.HTTP_400_BAD_REQUEST)

            user, created = User.objects.get_or_create(email=email, defaults={
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "role": "owner",  # or ask frontend to include role
            })

            if created:
                user.set_unusable_password()
                user.save()

            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                    "role": user.role
                }
            })

        except ValueError as e:
            return Response({"detail": "Invalid token", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OwnerRegisterView(generics.CreateAPIView):
    serializer_class = OwnerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
