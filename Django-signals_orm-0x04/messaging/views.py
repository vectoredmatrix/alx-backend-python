from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serial import MessageSerial
from .models import Message
 

# Create your views here.

class messageView(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerial
    
    