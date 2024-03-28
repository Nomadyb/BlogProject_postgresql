from django.db import models
from django.utils import timezone
from users.models import User

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_name = models.CharField(max_length=100)
    article = models.TextField()
    publish_date = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)
    # publish_date = models.DateTimeField()
    #TODO: boş olsun admin onayı olacak 
    # publish_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    #TODO: update_date kullanma autonow
    # update_date = models.DateTimeField()
    # update_date = models.DateTimeField(auto_now=True)
