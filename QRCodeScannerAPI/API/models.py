from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=1024)
    hash = models.CharField(max_length=45)
    User = models.ForeignKey(User, models.CASCADE)