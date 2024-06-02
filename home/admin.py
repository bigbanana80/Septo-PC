from django.contrib import admin
from . import models


class blog(admin.ModelAdmin):
    # settings here
    list_display = ["id", "title", "date_published"]


# Register your models here.
admin.site.register(models.blog, blog)
