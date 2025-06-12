from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import VeterinarianSerializer

User = get_user_model()

class VeterinarianViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = VeterinarianSerializer
