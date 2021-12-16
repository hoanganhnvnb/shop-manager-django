from rest_framework import serializers

from cart.models import Cart, CartItems
from user.serializers import SimpleUserSerializer
from items.serializers import ItemsSerializers


class CartSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ('id', 'user', 'create_at', 'update_at', 'active')

class CartCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ('id', 'user', )


class CartItemsSerializers(serializers.ModelSerializer):

    class Meta:
        model = CartItems
        fields = ('id', 'cart', 'items', 'quantity', )
        
class GetCartItemsSerializers(serializers.ModelSerializer):
    items = ItemsSerializers()
    class Meta:
        model = CartItems
        fields = ('id', 'cart', 'items', 'quantity', )