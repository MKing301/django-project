from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    inserted_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-inserted_date']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, related_name='usernames', on_delete=models.CASCADE)
    body = models.TextField()
    comment_inserted_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['comment_inserted_date']