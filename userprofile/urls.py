from rest_framework.routers import SimpleRouter
from .views import ProfileViewSet

profile_router = SimpleRouter()
profile_router.register('profile', ProfileViewSet)