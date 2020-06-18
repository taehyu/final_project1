from rest_framework import routers
from contents.views import ContentViewSet

router = routers.SimpleRouter()
router.register('contents', ContentViewSet)
urlpatterns = router.urls