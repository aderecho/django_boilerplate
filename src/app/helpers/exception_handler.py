from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        detail = response.data
        message = "Request failed."

        if isinstance(detail, dict) and "detail" in detail:
            message = str(detail["detail"])
        elif isinstance(detail, list):
            message = "Validation failed."
        elif isinstance(detail, dict):
            message = "Validation failed."

        return Response(
            {
                "success": False,
                "message": message,
                "errors": detail,
            },
            status=response.status_code,
        )

    if isinstance(exc, DjangoValidationError):
        return Response(
            {
                "success": False,
                "message": "Validation failed.",
                "errors": exc.message_dict if hasattr(exc, "message_dict") else exc.messages,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    if isinstance(exc, (AuthenticationFailed, NotAuthenticated)):
        return Response(
            {
                "success": False,
                "message": "Authentication failed.",
                "errors": {"detail": str(exc)},
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )

    if isinstance(exc, PermissionDenied):
        return Response(
            {
                "success": False,
                "message": "You do not have permission to perform this action.",
                "errors": {"detail": str(exc)},
            },
            status=status.HTTP_403_FORBIDDEN,
        )

    return Response(
        {
            "success": False,
            "message": "Internal server error.",
            "errors": {"detail": str(exc)},
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
