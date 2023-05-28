from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from userprofile.models import Profile
from .models import Post
from .serializers import PostSerializer, ListPostSerializer
JWT_authenticator = JWTAuthentication()

class PostViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def create(self, request, *args, **kwargs):
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            user, token = response

            try:
                profile = Profile.objects.get(user = token['user_id'])

            except Profile.DoesNotExist:
                error_data = {
                'error': 'Profile does not exist',
                'detail': 'The profile associated with the user does not exist.'
                }
                return Response(error_data, status=status.HTTP_400_BAD_REQUEST) 
            
            request.data['author'] = profile.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


    def list(self, request, *args, **kwargs):
        response = JWT_authenticator.authenticate(request)
        user, token = response
        
        try:
                profile = Profile.objects.get(user = token['user_id'])

        except Profile.DoesNotExist:
                error_data = {
                'error': 'Profile does not exist',
                'detail': 'The profile associated with the user does not exist.'
                }
                return Response(error_data, status=status.HTTP_400_BAD_REQUEST) 
        following_profiles = profile.followerdata.all()
        following_ids = following_profiles.values_list('followed_id', flat=True)
        posts = Post.objects.filter(author__in=following_ids)
        querysetFilter = self.filter_queryset(posts)
        page = self.paginate_queryset(querysetFilter)
        serializer = ListPostSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)