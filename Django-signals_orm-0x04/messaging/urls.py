from rest_framework.routers import DefaultRouter
from .views import messageView , delete_user
app_name = "messaging"

router = DefaultRouter()

router.register("messages" ,messageView , basename="messages" )
router.register("delete" , delete_user , basename="delete_user" )
urlpatterns = router.urls
