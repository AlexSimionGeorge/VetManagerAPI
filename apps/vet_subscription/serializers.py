from rest_framework import serializers
from .models import VetSubscription


class VetSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetSubscription
        fields = '__all__'
