from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    ROLES = (
        ("ADMIN", "Admin"),
        ("BLOGGER", "Blogger"),
    )
    # role = models.CharField(max_length=10, choices=ROLES)
    role = models.CharField(max_length=7, choices=ROLES, default="BLOGGER")

    def __str__(self):
        return self.email
