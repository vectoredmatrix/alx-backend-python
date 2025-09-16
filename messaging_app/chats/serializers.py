from .models import *
from rest_framework import serializers
from django.contrib.auth.hashers import make_password 

class Users (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs ={"password" :{"write_only":True}}
        
    
    def create(self , validated_data):
        password = validated_data.get("password")
        validated_data["password"] = make_password(password)
        # user = User(**validated_data)
        
        #user.set_password(password)
        #user.save()
        return super().create(validated_data)
    
    
class MessageSerial(serializers.ModelSerializer):
    sender_id = serializers.PrimaryKeyRelatedField(queryset = User.objects.all() , source = "sender_id" , write_only = True)
    
    class Meta:
        model = Message
        fields = ["message_id" , "message_body","sent_at" ,"sender_id"]


class ConvsersionSerial(serializers.ModelSerializer):
    participant = User(read_only = True , source = "participant_id")
    participant_id = serializers.PrimaryKeyRelatedField(queryset = User.objects.all() , source = "participant_id" , write_only = True)
    
    
    class Mata:
        model = Conversation
        fields = ["conversation_id" , "created_at" , "participant" , "participant_id"]
        



