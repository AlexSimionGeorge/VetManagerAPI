from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from apps.accounts.serializers import UserSerializer
from apps.accounts.models import User
from rest_framework import generics
from .serializers import LoginSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from apps.veterinarian.serializers import VeterinarianSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from apps.owner.serializers import OwnerSerializer

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

class OwnerRegisterView(generics.CreateAPIView):
    serializer_class = OwnerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
