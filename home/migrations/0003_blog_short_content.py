# Generated by Django 5.0.6 on 2024-05-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_blog_like_count_blog_view_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="short_content",
            field=models.TextField(default=""),
        ),
    ]