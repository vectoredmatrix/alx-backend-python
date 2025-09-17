from django.urls import path
from .views import ConversationViewset , MessageViewSet
app_name = "chats"


urlpatterns = [
    path("conversation/" , view=ConversationViewset.as_view() , name=ConversationViewset.name) ,
    
    path("messages/" , view=MessageViewSet.as_view(),
    name=MessageViewSet.name)
    
]
