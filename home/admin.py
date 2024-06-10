from django.contrib import admin
from . import models


class blog(admin.ModelAdmin):
    # settings here
    list_display = ["id", "title", "date_published"]


class contact(admin.ModelAdmin):
    # settings here
    list_display = ["email", "subject", "message"]


# Register your models here.
admin.site.register(models.blog, blog)
admin.site.register(models.contact, contact)
