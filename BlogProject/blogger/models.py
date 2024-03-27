from django.db import models
from django.utils import timezone
from users.models import User

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_name = models.CharField(max_length=100)
    article = models.TextField()
    # publish_date = models.DateField()
    publish_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
