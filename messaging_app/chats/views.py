from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.


class ConversationViewset(generics.ListAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConvsersationSerial
    name = "ConversationViewset"
    

class MessageViewSet(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerial
    name = "MessageViewSet"    