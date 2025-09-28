# chats/middleware.py
import logging
from datetime import datetime

from django.http import HttpResponseForbidden

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


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get current server hour (24-hour format)
        current_hour = datetime.now().hour  

        # Restrict if outside 6 AM - 9 PM
        if current_hour < 6 or current_hour >= 21:
            return HttpResponseForbidden("Access to the chat is restricted during this time.")

        # Otherwise continue as normal
        response = self.get_response(request)
        return response