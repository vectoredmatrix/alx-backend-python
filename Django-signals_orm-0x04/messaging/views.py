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




User = get_user_model()

# Create your views here.

class messageView(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerial
    


class delete_user (ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerial
    
    permission_classes = [IsAuthenticated]
    
    def destroy(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs["pk"]) 
        user.delete()
        return Response({"details":f"{user.username} accout has be deleted","status":"successful"} , status=status.HTTP_204_NO_CONTENT)