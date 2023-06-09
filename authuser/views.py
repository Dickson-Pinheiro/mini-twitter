from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authentication import RemoteUserAuthentication
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes= (RemoteUserAuthentication,)
    permission_classes=(AllowAny,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(email=request.data['email'],
                                  password=request.data['password'],
                                  username=request.data['username']
                                  )
        return Response(status=status.HTTP_201_CREATED)