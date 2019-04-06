from rest_framework import routers
from foxbinaryapi.api import TickHistoryViewSet

router = routers.DefaultRouter()
router.register('api/tickhistory', TickHistoryViewSet, 'tickhistory')

urlpatterns = router.urls