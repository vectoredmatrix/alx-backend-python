from django.dispatch import receiver
from .models import Message , Notification , MessageHistory
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save , pre_save

app_name = "messaging"
User = get_user_model()



@receiver(post_save , sender = Message)

def notify_user(sender , instance , created , **kwargs):
    
    if created:
        print(instance.sender.id)
        receiver = instance.receiver
        sender = instance.sender
        Notification.objects.create(
            user = receiver,
            sent_by = sender,
            new_message = True,
            message = instance
        )
        print(f"{receiver.username} you have a new message from {sender.username}")
        

@receiver(pre_save , sender = Message)
def track_edited_message(sender , instance , **kwargs):
    if instance.pk:
        pk = instance.pk
        try:
           
            obj = Message.objects.get(pk = pk)
        except Message.DoesNotExist:
            return
            
        
        
        else:
            old_content = obj.content
            if old_content != instance.content:
                MessageHistory.objects.create(
                    edited = True,
                    message = instance,
                    old_content = old_content
                )
            print(f"{instance.sender} edited the message")
                


