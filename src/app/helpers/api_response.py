from rest_framework.response import Response

class ApiResponse:
    @staticmethod
    def success(message="Success", data=None, meta=None, status_code=200):
        return Response({
            "success": True,
            "message": message,
            "data": data,
            "meta": meta or {},
        }, status=status_code)

    @staticmethod
    def error(message="Error", errors=None, status_code=400):
        return Response({
            "success": False,
            "message": message,
            "errors": errors or {},
        }, status=status_code)
