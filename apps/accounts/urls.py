from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import VeterinarianRegisterView, LoginView, OwnerRegisterView, GoogleLoginView

urlpatterns = [
    path('register/veterinarian/', VeterinarianRegisterView.as_view(), name='register_veterinarian'),
    path('register/owner/', OwnerRegisterView.as_view(), name='register_owner'),
    path('login/', LoginView.as_view(), name='login'),
    path("login/google/", GoogleLoginView.as_view(), name="google-login"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
