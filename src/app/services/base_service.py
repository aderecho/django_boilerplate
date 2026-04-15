class BaseService:
    @staticmethod
    def success(data=None, message="Success", status_code=200, meta=None):
        return {
            "success": True,
            "message": message,
            "data": data,
            "meta": meta or {},
            "status_code": status_code,
        }

    @staticmethod
    def error(message="Something went wrong.", errors=None, status_code=400):
        return {
            "success": False,
            "message": message,
            "errors": errors or {},
            "status_code": status_code,
        }
