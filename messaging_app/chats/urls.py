from rest_framework import routers
from .views import *
from django.urls import include ,path

app_name = "chats"

router = routers.DefaultRouter()

router.register("conversation" , ConversationViewset , basename=ConversationViewset.name)
router.register("message" , MessageViewSet , basename=MessageViewSet.http_method_names)

urlpatterns = [
    path("" , include("router.urls"))
    
]
