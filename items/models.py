from django.db import models

from category.models import Category
# Create your models here.

class Items(models.Model):
    barcode = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    importPrice = models.IntegerField(default=0)
    sellPrice = models.IntegerField(default=0)

    quantity = models.IntegerField(default=0)

    companyName = models.CharField(max_length=50)

    active = models.BooleanField(default=True)
    
    quantity_sold = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)

# class ItemsCategory(models.Model):
#     items = models.ForeignKey(Items)
#     category = models.ForeignKey(Category)


