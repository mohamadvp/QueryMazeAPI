from rest_framework import serializers
from .orderSerializers import OrderByCustomerSerializers
from .productSerializers import ProductSerializer
from querymaze.models import Customer, Order, OrderItem

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

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only= True)
    class Meta:
        model = OrderItem
        fields = ['product','qty','unit_price']

class OrderReportSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source = 'customer.name') 
    item = OrderItemSerializer(source='orderitem_set',many= True, read_only = True)
    
    class Meta:
        model = Order
        fields = ['orderid','ordered','customer_name','item']