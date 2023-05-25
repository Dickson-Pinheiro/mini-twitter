from django.db import models
from userprofile.models import Profile

class Base(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True

class Post(Base):
    author = models.ForeignKey(Profile, related_name='authordata', on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        ordering=['-created_at']
