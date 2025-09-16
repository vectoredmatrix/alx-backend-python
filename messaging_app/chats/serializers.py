from .models import *
from rest_framework import serializers

class Users (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs ={"password" :{"write_only":True}}
        
    
    def create(self , validated_data):
        password = validated_data.pop("password")
        
        user = User.objects.create(**validated_data)
        
        #user.set_password(password)
        user.save()
        return user
    
    



