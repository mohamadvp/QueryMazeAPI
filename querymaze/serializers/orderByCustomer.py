from rest_framework import serializers
from ..models import Customer,Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customerid', 'name']


class OrderByCustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['orderid','ordered','total']

class CustomerNoOrderSerializers(serializers.ModelSerializer):
    orders = OrderByCustomerSerializers(many=True, read_only=True, source='order_set')
    class Meta:
        model = Customer
        fields = ['orders','name']