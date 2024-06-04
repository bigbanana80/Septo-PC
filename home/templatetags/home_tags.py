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
        "last_post1": blogs[0],
        "last_post2": blogs[1],
        "last_post3": blogs[2],
        "last_post4": blogs[3],
        "last_post5": blogs[4],
        "last_post6": blogs[5],
    }
    return c
