# Generated by Django 5.0.2 on 2024-04-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogger", "0006_alter_blog_publish_date_alter_blog_update_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="status",
            field=models.CharField(default="waiting", max_length=20),
        ),
    ]
