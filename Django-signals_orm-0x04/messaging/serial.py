from rest_framework.serializers import ModelSerializer , SerializerMethodField
from .models import *
from django.contrib.auth import get_user_model



class MessageSerial(ModelSerializer):
    sender = SerializerMethodField()
    receiver = SerializerMethodField()
    class Meta:
        model = Message
        fields = "__all__"
        

    def get_sender(self ,obj):
        return obj.sender.username
     
    def get_reciever(self ,obj):
        return obj.receiver.username