from django.contrib import admin

# Register your models here.
from .models import Message ,MessageHistory ,Notification




class MessageAdmin(admin.ModelAdmin):
    list_display =["sender" , "receiver" , "content" , "parent_message"]
    


class EditedMessage(admin.ModelAdmin):
    list_display = ["edited_at" , "edited_by", 
                    "edited" , "old_content"]

class NotificationAdmin(admin.ModelAdmin):
    list_display = [ "user" ,"new_message" ,"sent_by"]    

admin.site.register(Message , MessageAdmin)
admin.site.register(MessageHistory, EditedMessage)
admin.site.register(Notification , NotificationAdmin)