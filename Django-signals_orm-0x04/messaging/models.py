from django.db import models
from django.conf import settings
# Create your models here.
from .managers import UnreadMessagesManager


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name="sent_messages")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE , related_name="received_messages")
    content = models.TextField(max_length=5000 , blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    unread = UnreadMessagesManager()
    

    parent_message = models.ForeignKey(
        "self",
        on_delete=models.CASCADE, 
        related_name="replies" ,
        null= True , 
        blank=True
        )

    def __str__(self) -> str:
        return f"{self.sender.username} -> {self.receiver.username}"
    
    
class Notification(models.Model):
    unread= models.BooleanField(default=False , blank = False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name="notifications")
    sent_by = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name="sent_notification")
    message = models.ForeignKey(Message , on_delete=models.CASCADE ,related_name="notifications")
    
  
class MessageHistory(models.Model):
    edited = models.BooleanField(default=False) 
    message = models.ForeignKey(Message , on_delete=models.CASCADE, related_name="edits")
    old_content = models.TextField(max_length=5000 , blank=False)
    edited_at = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name="edited_histories")
    