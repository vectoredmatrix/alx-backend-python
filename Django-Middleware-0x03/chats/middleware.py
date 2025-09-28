# chats/middleware.py
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get user (Anonymous if not logged in)
        user = request.user if request.user.is_authenticated else "Anonymous"

        # Log to file
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")

        # Continue request/response cycle
        response = self.get_response(request)
        return response
