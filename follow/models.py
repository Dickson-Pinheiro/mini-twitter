from django.db import models
from django.core.exceptions import ValidationError
from userprofile.models import Profile


class Base(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        
        abstract = True


class Follow(Base):

    follower = models.ForeignKey(Profile, related_name='followerdata', on_delete=models.CASCADE)
    followed = models.ForeignKey(Profile, related_name='followeddata', on_delete=models.CASCADE)

    class Meta:

        unique_together = ['follower', 'followed']
