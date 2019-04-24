from rest_framework import routers
from foxbinaryapi.api import TickHistoryViewSet, BlogPostViewSet

router = routers.DefaultRouter()
router.register('api/tickhistory', TickHistoryViewSet, 'tickhistory')
router.register('api/blogs', BlogPostViewSet, 'blogposts')

urlpatterns = router.urls