from rest_framework import viewsets
from .models import VetSubscription
from .serializers import VetSubscriptionSerializer

class VetSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = VetSubscription.objects.all()
    serializer_class = VetSubscriptionSerializer
