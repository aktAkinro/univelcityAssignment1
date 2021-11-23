from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# abstract user is an already created by django
class CustomUser(AbstractUser):
    address = models.TextField(null=True, blank=True)
    
