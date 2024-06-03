from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_tumb", null=True)
    category = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    publish_date = models.DateTimeField(blank=False, default=timezone.now)

    @property
    def is_past_due(self):
        return timezone.now() > self.date_published

    def __str__(self) -> str:
        return self.title
