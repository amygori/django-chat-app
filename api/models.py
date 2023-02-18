from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Pet(models.Model):
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=255)
  owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="pets")


