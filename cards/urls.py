from rest_framework import routers

from cards.views import CardViewSet

router = routers.SimpleRouter()
router.register('cards/', CardViewSet)
urlpatterns = router.urls