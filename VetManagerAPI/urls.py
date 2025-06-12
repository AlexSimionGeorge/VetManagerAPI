from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/owners/', include('apps.owner.urls')),
    path('api/veterinarians/', include('apps.veterinarian.urls')),
    path('api/animals/', include('apps.animal.urls')),
    path('api/vet_subscriptions/', include('apps.vet_subscription.urls'))
]
