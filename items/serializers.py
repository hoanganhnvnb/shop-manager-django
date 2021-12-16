from rest_framework import serializers

from category.serializers import CategorySerializers, CategoryCreateSerializers
from .models import Items


class ItemsSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Items
        fields = ('id', 'barcode', 'title', 'description', 'category', 'image'
                  , 'importPrice', 'sellPrice', 'quantity', 'companyName', 'active', 'quantity_sold')
        
    def get_image(self, items):
        return items.image.url

class ItemsCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id', 'barcode', 'title', 'description', 'category', 'image'
                  , 'importPrice', 'sellPrice', 'quantity', 'companyName', 'active', 'quantity_sold')

class ItemsAddQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('quantity', )

class ItemsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('image', )
