from django.db import models



class UnreadMessagesManager(models.Manager):
    def unread(self , request):
        return self.filter(receiver= request , notifications__new_message = True)
