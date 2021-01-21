from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField()
    id = models.CharField(max_length=45)