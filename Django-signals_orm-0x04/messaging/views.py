from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serial import MessageSerial
from .models import Message
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from chats.serializers import UserSerial
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page





User = get_user_model()

# Create your views here.

class messageView(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerial
    
    def get_queryset(self):
        user = self.request.user #sender=request.user
        
        
        queryset = (
                    Message.objects.filter(Q(sender=user) | Q(receiver = user),  )
                    .select_related("sender", "receiver","parent_message")
                    .prefetch_related("replies", "edits")
                    
)
        
        return queryset.distinct()
    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
        
    
    
class UnreadMessages(ModelViewSet):
    
    serializer_class = MessageSerial
    permission_classes = [IsAuthenticated]

   
    def get_queryset(self):
        user = self.request.user
        unread = Message.unread.unread_for_user(user).only("sender__username" , "receiver__username","content" , "timestamp")
        return unread
    
       
   



class delete_user (ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerial
    
    permission_classes = [IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs["pk"]) 
        user.delete()
        return Response({"details":f"{user.username} accout has be deleted","status":"successful"} , status=status.HTTP_204_NO_CONTENT)