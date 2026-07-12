def success_response(data=None, message="Success"):
    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(message="Error", code=400):
    return {
        "success": False,
        "error": {
            "message": message,
            "code": code
        }
    }