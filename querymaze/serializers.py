from rest_framework import serializers
from .models import Customer,Product,Order,OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    total_number = serializers.IntegerField()
    total_spent  = serializers.DecimalField(max_digits=20 , decimal_places=3)
    last_order = serializers.DateTimeField()
    class Meta:
        model = Customer
        fields = ['name','phone','birthdate','total_number','total_spent','last_order']

class TopCustomerSerializer(serializers.ModelSerializer):
    total_spent  = serializers.DecimalField(max_digits=20 , decimal_places=3)
    class Meta:
        model = Customer
        fields = ['name','phone','total_spent']

class MiniCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','phone']

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

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only= True)
    class Meta:
        model = OrderItem
        fields = ['product','qty','unit_price']


class OrderSerializer(serializers.ModelSerializer):
    # customer_name = serializers.SerializerMethodField()
    # customer_phone = serializers.SerializerMethodField()
    customer = MiniCustomerSerializer(read_only = True)
    orderitem_set = OrderItemSerializer(many= True, read_only = True)

    class Meta:
        model = Order
        fields = ['orderid', 'ordered','customer','orderitem_set']

    # def get_customer_name(self, obj):
    #     return obj.customer.name

    # def get_customer_phone(self, obj):
    #     return obj.customer.phone


class OrderReportSerializer(serializers.ModelSerializer):
    customer = MiniCustomerSerializer(read_only= True)
    orderitem_set = OrderItemSerializer(many= True, read_only = True)
    
    class Meta:
        model = Order
        fields = ['orderid','ordered','customer','orderitem_set']