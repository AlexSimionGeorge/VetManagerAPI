# Django REST Framework
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
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
    permission_classes = [AllowAny]
    serializer_class = VeterinarianSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OwnerRegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = OwnerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

class GoogleLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        token = request.data.get("google_token")
        if not token:
            return Response({"detail": "Missing ID token"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

            # Extract info
            email = idinfo.get("email")
            if not email:
                return Response({"detail": "Email not provided by Google."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response(
                    {"detail": "Account does not exist."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # User exists: issue token
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
            return Response(
                {"detail": "Invalid token", "error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


