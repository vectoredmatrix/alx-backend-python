from django.db import models



class UnreadMessagesManager(models.Manager):
    def unread_for_user(self , request):
        return self.filter(receiver= request , notifications__unread= True)
