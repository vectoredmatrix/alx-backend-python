from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import include

app_name = "chats"

route = DefaultRouter()

route.register("conversation" , ConversationViewset , basename=ConversationViewset.name)
route.register("message" , MessageViewSet , basename=MessageViewSet.http_method_names)

urlpatterns = [
    "" , include("route.urls")
    
]
