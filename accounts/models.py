from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_image = ProcessedImageField(
        blank = True,
        format = 'JPEG',
        processors = [Thumbnail(200, 200)],
        options = {'quality': 90},
    )
    introduction = models.TextField(blank=True)
