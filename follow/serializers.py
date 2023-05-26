from rest_framework import serializers
from .models import Follow

class FollowSerializer(serializers.ModelSerializer):

    class Meta:

        model = Follow

        fields = ('follower', 'followed')

    def validate(self, attrs):
        follower = attrs.get('follower')
        followed = attrs.get('followed')

        if follower == followed:
            raise serializers.ValidationError("You cannot follow yourself")

        return attrs
