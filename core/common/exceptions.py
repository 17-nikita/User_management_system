# core/exceptions.py
from fastapi import HTTPException, status

# ---- 400 Bad Request ----
def bad_request(detail: str = "400:Bad request"):
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=detail
    )

# ---- 401 Unauthorized ----
def unauthorized(detail: str = "Unauthorized"):
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail
    )

# ---- 404 Not Found ----
def not_found(detail: str = "404:Resource not found"):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=detail
    )

# ---- 500 Internal Server Error ----
def internal_server_error(detail: str = "Internal server error"):
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=detail
    )
