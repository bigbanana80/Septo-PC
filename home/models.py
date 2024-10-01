from django.db import models
from datetime import datetime
from django.utils import timezone
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'title': self.title})
    
    def __str__(self) -> str:
        return self.title


class contact(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=False)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=False)

class user(models.Model):
    username = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255,blank=False)
    password = models.CharField(max_length=255,blank=False)