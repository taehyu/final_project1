from rest_framework import routers
from cards.views import CardViewSet
from users.views import UserViewSet
from contents.views import ContentViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register('users', UserViewSet)
router.register('cards', CardViewSet)
router.register('contents', ContentViewSet)
urlpatterns = router.urls
