from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.owner.urls')),
    path('api/', include('apps.veterinarian.urls')),
    path('api/', include('apps.animal.urls')),

    path('api/', include('apps.vet_subscription.urls')),
]
