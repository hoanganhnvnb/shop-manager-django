from rest_framework import serializers

from .models import Report
class ReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Report
        fields = ('id', 'total_price_import', 'total_price_sell', 'new_cus', 'count_nv', )