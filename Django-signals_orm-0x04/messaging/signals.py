from django.dispatch import receiver
from .models import Message , Notification
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()



@receiver(post_save , sender = Message)

def notify_user(sender , instance , created , **kwargs):
    
    if created:
        receiver = instance.receiver
        sender = instance.sender
        Notification.objects.create(
            user = receiver,
            from_ = sender,
            new_message = True
        )
        print(f"{receiver} you have a new message from {sender}")