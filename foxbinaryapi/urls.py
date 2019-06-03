from rest_framework import routers
from foxbinaryapi.api import TickHistoryViewSet, BlogPostViewSet, APITokenViewSet

router = routers.DefaultRouter()
router.register('api/tickhistory', TickHistoryViewSet, 'tickhistory')
router.register('api/blogs', BlogPostViewSet, 'blogposts')
router.register('api/token', APITokenViewSet, 'apitokens')

urlpatterns = router.urls