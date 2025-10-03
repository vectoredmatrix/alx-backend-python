from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Message(models.Model):
    sender = models.ForeignKey(User , on_delete=models.CASCADE , related_name="sender")
    reciever = models.ForeignKey(User , on_delete= models.CASCADE , related_name="reciever")
    content = models.TextField(max_length=5000 , blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    