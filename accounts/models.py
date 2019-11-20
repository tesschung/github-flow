from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# User 모델을 Customizing 한다.
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='followings'
    )