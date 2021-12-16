from rest_framework import serializers

from category.serializers import CategorySerializers, CategoryCreateSerializers
from .models import Items


class ItemsSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ('id', 'barcode', 'title', 'description', 'category', 'image'
                  , 'importPrice', 'sellPrice', 'quantity', 'companyName', 'active', 'quantity_sold')
        
    def get_image(self, items):
        request = self.context.get('request')
        photo_url = items.image.url
        return request.build_absolute_uri(photo_url)

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
