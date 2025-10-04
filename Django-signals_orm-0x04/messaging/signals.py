from django.dispatch import receiver
from .models import Message , Notification , MessageHistory
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save , pre_save , post_delete

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
                    old_content = old_content,
                    edited_by = obj.sender
                )
            print(f"{instance.sender} edited the message")
                


@receiver(post_delete , sender = User)
def notify_user_before_account_deletion(sender , instance ,**kwargs ):
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    Notification.objects.filter(user=instance).delete()
    Notification.objects.filter(sent_by=instance).delete()

    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()

    print(f"{instance.username} accoount has being deleted")