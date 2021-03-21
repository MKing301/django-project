from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    inserted_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-inserted_date']