from rest_framework.permissions import BasePermission


class IsParticipantOfConversation(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
       
        return obj.participants_id == request.user
    
    
class IsSenderOfMessage(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        
        return obj.sender_id == request.user
    