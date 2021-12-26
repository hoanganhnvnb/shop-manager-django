from django.db import models

# Create your models here.

class SearchText(models.Model):
    search_text = models.CharField(default='', max_length=255)