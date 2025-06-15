from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import VeterinarianRegisterView, LoginView

urlpatterns = [
    path('register/veterinarian/', VeterinarianRegisterView.as_view(), name='register_veterinarian'),
    # Later add: path('register/owner/', OwnerRegisterView.as_view(), name='register_owner'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
