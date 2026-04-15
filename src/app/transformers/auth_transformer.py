from app.serializers.auth_serializer import UserSerializer

class AuthTransformer:
    @staticmethod
    def transform_payload(payload):
        if not payload:
            return None
        return {
            "user": UserSerializer(payload["user"]).data,
            "tokens": payload["tokens"],
        }
