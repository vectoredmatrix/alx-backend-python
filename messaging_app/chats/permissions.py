from rest_framework.permissions import BasePermission


class IsParticipantOfConversation(BasePermission):
    
    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in ("GET","HEAD" ,"OPTIONS"):
            return True
        
        return obj.owner == request.user
    