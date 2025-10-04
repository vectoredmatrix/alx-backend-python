from rest_framework.routers import DefaultRouter
from .views import messageView
app_name = "messaging"

router = DefaultRouter()

router.register("messages/" ,messageView , basename="messages" )

urlpatterns = router.urls
