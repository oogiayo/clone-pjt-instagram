from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    like_post = models.ManyToManyField('self', related_name='like_user')
    following = models.ManyToManyField('self', related_name='follower')
