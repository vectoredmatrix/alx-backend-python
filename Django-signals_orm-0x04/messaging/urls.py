from rest_framework.routers import DefaultRouter
from .views import messageView , delete_user, UnreadMessages
app_name = "messaging"

router = DefaultRouter()

router.register("messages" ,messageView , basename="messages" )
router.register("delete" , delete_user , basename="delete_user" )
router.register("unread",UnreadMessages ,basename= "unread")


urlpatterns = router.urls
