from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Follow
from .serializers import FollowSerializer
from userprofile.models import Profile


JWT_authenticator = JWTAuthentication()

class FollowViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
                    ):

    queryset = Follow.objects.all()
    serializer_class= FollowSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def create(self, request, *args, **kwargs):
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            user, token = response
            profile = Profile.objects.filter(user = token['user_id'])
            request.data['follower'] = profile.get().id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
