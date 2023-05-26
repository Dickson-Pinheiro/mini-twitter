from rest_framework.routers import SimpleRouter
from .views import FollowViewSet

follow_router = SimpleRouter()
follow_router.register('follow', FollowViewSet)