from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView

from app.serializers.auth_serializer import (
    LoginSerializer,
    LogoutSerializer,
    RegisterSerializer,
    UserSerializer,
)
from app.services.auth_service import AuthService
from app.transformers.auth_transformer import AuthTransformer

class RegisterController(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=RegisterSerializer,
        responses={201: UserSerializer},
        tags=["Auth"],
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = AuthService.register(serializer.validated_data)
        return Response(
            {
                "success": result["success"],
                "message": result["message"],
                "data": AuthTransformer.transform_payload(result["data"]),
            },
            status=result["status_code"],
        )

class LoginController(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=LoginSerializer,
        tags=["Auth"],
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = AuthService.login(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        payload = result.get("data")
        return Response(
            {
                "success": result["success"],
                "message": result["message"],
                "data": AuthTransformer.transform_payload(payload) if payload else None,
            },
            status=result["status_code"],
        )

class LogoutController(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=LogoutSerializer,
        tags=["Auth"],
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = AuthService.logout(serializer.validated_data["refresh"])
        body = {
            "success": result["success"],
            "message": result["message"],
        }
        if "errors" in result:
            body["errors"] = result["errors"]
        return Response(body, status=result["status_code"])

class MeController(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=["Auth"])
    def get(self, request):
        return Response({
            "success": True,
            "message": "Authenticated user fetched successfully.",
            "data": UserSerializer(request.user).data,
        })

class CustomTokenRefreshController(TokenRefreshView):
    permission_classes = [AllowAny]
