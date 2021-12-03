from rest_framework import serializers

from category.models import Category


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'description', 'active')

class CategoryCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'description', 'active')
