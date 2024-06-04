from django import template

from home.models import blog
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.utils import timezone

register = template.Library()


@register.inclusion_tag("latest_post.html")
def latest_post():
    blogs = blog.objects.filter(publish_date__lte=timezone.now(), status=True).order_by(
        "-publish_date"
    )[:6:1]
    c = {
        "last_post_page1": [x for x in blogs[0:3]],
        "last_post_page2": [x for x in blogs[3:6]],
    }
    return c
