from rest_framework import viewsets, parsers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.settings import api_settings
from jwt import decode
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Profile
from .serializers import ProfileSerializer

JWT_authenticator = JWTAuthentication()

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def create(self, request, *args, **kwargs):
        token = request.auth
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            user, token = response
            request.data['user'] = token['user_id']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        token = request.auth
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            user, token = response
            print(user)
        return Response(status=status.HTTP_200_OK)
