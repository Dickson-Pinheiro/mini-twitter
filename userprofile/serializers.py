from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields =  (
            'id',
            'first_name',
            'user',
            'last_name',
            'profile_picture',
        )

