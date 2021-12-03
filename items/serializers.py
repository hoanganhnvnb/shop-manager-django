from rest_framework import serializers

from category.serializers import CategorySerializers
from .models import Items


class ItemsSerializers(serializers.ModelSerializer):
    category = CategorySerializers()

    class Meta:
        model = Items
        fields = ('id', 'barcode', 'title', 'description', 'category'
                  , 'importPrice', 'sellPrice', 'quantity', 'companyName', 'active')

class ItemsCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('barcode', 'title', 'description', 'category'
                  , 'importPrice', 'sellPrice', 'quantity', 'companyName', 'active')