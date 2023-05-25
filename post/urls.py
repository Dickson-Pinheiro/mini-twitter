from rest_framework.routers import SimpleRouter
from .views import PostViewSet

post_router = SimpleRouter()
post_router.register('post', PostViewSet)