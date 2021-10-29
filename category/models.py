from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.CharField(max_length=100, default=100)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
