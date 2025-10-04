from django.contrib import admin

# Register your models here.
from .models import Message ,MessageHistory



class MessageAdmin(admin.ModelAdmin):
    list_display =["sender" , "receiver" , "content"]
    


class EditedMessage(admin.ModelAdmin):
    list_display = ["edited_at" , "edited_by", 
                    "edited" , "old_content"]
    

admin.site.register(Message , MessageAdmin)
admin.site.register(MessageHistory, EditedMessage)