from django.db import models

from items.models import Items
from user.models import CustomerUser
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=0)
