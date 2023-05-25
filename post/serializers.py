from rest_framework import serializers
from userprofile.models import Profile
from django.contrib.auth.models import User
from .models import Post

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UsernameSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields =  (
            'profile_picture',
            'user',
        )


class PostSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Post

        fields = (
            'id',
            'content',
            'author'
        )