from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Tag(models.Model):
    content = models.CharField(max_length=10, unique=True)


class Post(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = ProcessedImageField(
        # upload_to="media/%Y/%m/%d",
        format = 'JPEG',
        processors = [ResizeToFill(633, 633)],
        options = {'quality': 90},
    )
    content = models.TextField()
    hashtags = models.ManyToManyField(Tag, related_name='taged_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


