from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    extra_kwargs = {'password': {'write_only': True}, 'id': {'read_only': True}}
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password')