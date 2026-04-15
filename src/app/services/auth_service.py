from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from app.models.token_blacklist import RefreshTokenBlacklist
from app.models.user import User
from app.services.base_service import BaseService

class AuthService(BaseService):
    @staticmethod
    def register(validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        refresh = RefreshToken.for_user(user)
        return AuthService.success(
            data={
                "user": user,
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
            },
            message="User registered successfully.",
            status_code=201,
        )

    @staticmethod
    def login(email, password):
        user = authenticate(username=email, password=password)
        if not user:
            return AuthService.error(
                message="Invalid credentials.",
                status_code=401,
            )

        refresh = RefreshToken.for_user(user)
        return AuthService.success(
            data={
                "user": user,
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
            },
            message="Login successful.",
        )

    @staticmethod
    def logout(refresh_token):
        try:
            token = RefreshToken(refresh_token)
            jti = token["jti"]
            exp_timestamp = token["exp"]
            expires_at = timezone.datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)

            RefreshTokenBlacklist.objects.get_or_create(
                jti=jti,
                defaults={
                    "user_id": token.get("user_id"),
                    "expires_at": expires_at,
                },
            )

            token.blacklist()
            return AuthService.success(message="Logout successful.")
        except TokenError:
            return AuthService.error(message="Invalid or expired refresh token.", status_code=400)
