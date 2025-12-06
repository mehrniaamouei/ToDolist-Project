from .base import BaseAppException


class ServiceError(BaseAppException):
    """Raised when service-level errors occur."""
    pass