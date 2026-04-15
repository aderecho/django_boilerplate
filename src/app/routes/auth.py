from django.urls import path
from app.controllers.auth_controller import (
    CustomTokenRefreshController,
    LoginController,
    LogoutController,
    MeController,
    RegisterController,
)

urlpatterns = [
    path("register/", RegisterController.as_view(), name="auth-register"),
    path("login/", LoginController.as_view(), name="auth-login"),
    path("refresh/", CustomTokenRefreshController.as_view(), name="auth-refresh"),
    path("logout/", LogoutController.as_view(), name="auth-logout"),
    path("me/", MeController.as_view(), name="auth-me"),
]
