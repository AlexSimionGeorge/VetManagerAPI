from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VetSubscriptionViewSet

router = DefaultRouter()
router.register(r'', VetSubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
