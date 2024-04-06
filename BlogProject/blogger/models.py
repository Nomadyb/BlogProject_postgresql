from users.models import User  # User modelini users uygulamasından içe aktar
from django.db import models
from django.utils import timezone

# class Blog(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     blog_name = models.CharField(max_length=100)
#     article = models.TextField()
#     publish_date = models.DateTimeField(null=True, blank=True)
#     #TODO: null olmalı update 
#     update_date = models.DateTimeField(null=True)
#     # publish_date = models.DateTimeField()
#     #TODO: boş olsun admin onayı olacak 
#     # publish_date = models.DateTimeField(default=timezone.now)
#     active = models.BooleanField(default=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     #TODO: update_date kullanma autonow
#     # update_date = models.DateTimeField()
#     # update_date = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=20, default='waiting')


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_name = models.CharField(max_length=100)
    article = models.TextField()
    # Admin onayı beklerken boş olabilir
    publish_date = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True)  # Null olabilir
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='waiting')
