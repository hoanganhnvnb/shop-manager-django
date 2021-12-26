from rest_framework import serializers
from .models import SearchText
class SearchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SearchText
        fields = ('search_text', )