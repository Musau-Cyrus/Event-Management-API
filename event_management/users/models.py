from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(
        max_length=10,
        choices=[("user", "user"), ("admin", "admin")],
        default="user"
    )
    created_at = models.DateTimeField(auto_now_add=True)