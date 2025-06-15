from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.veterinarian.models import Veterinarian
from apps.veterinarian.serializers import VeterinarianSerializer

class VeterinarianViewSet(viewsets.ModelViewSet):
    queryset = Veterinarian.objects.select_related("user").all()
    serializer_class = VeterinarianSerializer
    permission_classes = [IsAuthenticated]
