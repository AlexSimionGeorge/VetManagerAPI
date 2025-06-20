from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet

router = DefaultRouter()
router.register(r'', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
