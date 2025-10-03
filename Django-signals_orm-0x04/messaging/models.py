from django.db import models
from django.conf import settings
# Create your models here.



class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE , related_name="receiver")
    content = models.TextField(max_length=5000 , blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return f"{self.sender.username} -> {self.receiver.username}"
    
    
class Notification(models.Model):
    new_message = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    from_ = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    message = models.ForeignKey(Message , on_delete=models.CASCADE)
    
    
    