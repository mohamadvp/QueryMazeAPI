from rest_framework import serializers
from querymaze.models import Customer
from .orderSerializers import OrderByCustomerSerializers

class TopCustomerSerializers(serializers.ModelSerializer):
    total_spent = serializers.DecimalField(max_digits=20 , decimal_places=3, read_only = True)
    class Meta:
        model = Customer
        fields = ['customerid','name','phone','total_spent']

class CustomerNoOrderSerializers(serializers.ModelSerializer):
    orders = OrderByCustomerSerializers(many=True, read_only=True, source='order_set')
    class Meta:
        model = Customer
        fields = ['orders','name']