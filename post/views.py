from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from userprofile.models import Profile
from .models import Post
from .serializers import PostSerializer
JWT_authenticator = JWTAuthentication()

class PostViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def create(self, request, *args, **kwargs):
        token = request.auth
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            user, token = response
            profile = Profile.objects.filter(user = token['user_id'])
            request.data['author'] = profile.get().id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
