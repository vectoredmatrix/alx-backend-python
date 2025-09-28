# chats/middleware.py
import logging , time
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
    



class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Store request history: {ip: [timestamps]}
        self.request_log = {}

        # Config
        self.time_window = 60   # 1 minute
        self.max_requests = 5   # 5 messages per IP per minute

    def __call__(self, request):
        # Only apply to POST requests (messages)
        if request.method == "POST" and "/messages" in request.path.lower():
            ip = self.get_client_ip(request)
            now = time.time()

            # Get request timestamps for this IP
            timestamps = self.request_log.get(ip, [])

            # Remove timestamps older than 1 min
            timestamps = [t for t in timestamps if now - t < self.time_window]

            if len(timestamps) >= self.max_requests:
                return HttpResponseForbidden("Rate limit exceeded: Only 5 messages per minute allowed.")

            # Add current timestamp
            timestamps.append(now)
            self.request_log[ip] = timestamps

        return self.get_response(request)

    def get_client_ip(self, request):
        """Extract client IP from request headers or META"""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")
    
    
    

class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only check authenticated users
        if request.user.is_authenticated:
            # Assuming your User model has a 'role' field (e.g., "admin", "moderator", "user")
            user_role = getattr(request.user, "role", None)

            if user_role not in ["admin", "moderator"]:
                return HttpResponseForbidden("Access denied: insufficient permissions.")

        # Continue request-response cycle
        return self.get_response(request)

