from django.db import models

# Create your models here.

class Report(models.Model):
    total_price_import = models.IntegerField(default=0)
    total_price_sell = models.IntegerField(default=0)
    new_cus = models.IntegerField(default=0)
    count_nv = models.IntegerField(default=0)
