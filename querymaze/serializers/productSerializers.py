from rest_framework import serializers
from ..models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['desc','sku']

class BestSellingProductSerializer(serializers.ModelSerializer):
    total_qty = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=20, decimal_places=3)
    class Meta:
        model = Product
        fields = ['desc','sku','total_qty','total_revenue']