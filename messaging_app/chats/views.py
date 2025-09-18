from django.shortcuts import render
from rest_framework import viewsets , filters , status
from rest_framework.response import Response
from .models import *
from .serializers import *


# Create your views here.


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConvsersationSerial
    name = "ConversationViewset"
    filter_backends = [filters.SearchFilter]
    search_fields =  ["particapant__first_name","participant__lanst_name"]
    
    def create(self, request, *args, **kwargs):
        
        serial = self.get_serializer(data = request.data)
        if serial.is_valid():
            self.perform_create(serial)
            return Response({"Status":"success" , "data":serial.data} , status=status.HTTP_201_CREATED)
        
        return Response({"status":"Error" ,"Error":serial.errors } , status=status.HTTP_400_BAD_REQUEST)
            
    

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerial
    name = "MessageViewSet"  
    filter_backends = [filters.SearchFilter]
    search_fields = ["message_body"]
    
    def create(self, request, *args, **kwargs):
        
        serial = self.get_serializer(request.data)
        
        if serial.is_valid():
            self.perform_create(serial)
            
            return Response({
                "status":"Success" , "data":serial.data
            }, status=status.HTTP_201_CREATED) 
            
        return Response({"status": "error" , "Error":serial.errors} , status=status.HTTP_400_BAD_REQUEST)