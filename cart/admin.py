from django.contrib import admin

# Register your models here.
from cart.models import Cart, CartItems

admin.site.register(Cart)
admin.site.register(CartItems)