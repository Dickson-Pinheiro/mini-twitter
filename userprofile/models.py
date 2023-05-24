from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='userdata', on_delete=models.CASCADE, unique=models.UniqueConstraint)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture = models.FileField()
    
    def __str__(self) -> str:
        return self.first_name
