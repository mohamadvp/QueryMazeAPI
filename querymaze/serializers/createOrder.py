from rest_framework import serializers
from django.utils import timezone
from decimal import Decimal
from querymaze.models import Customer, Product, Order, OrderItem


class OrderCreateItemSerializer(serializers.Serializer):
    sku = serializers.CharField()
    qty = serializers.IntegerField(min_value=1)

class OrderCreateSerializer(serializers.Serializer):
    customer_id = serializers.CharField()
    items = OrderCreateItemSerializer(many = True)

    def validate_customer_id(self, value):
        if not Customer.objects.filter(pk=value).exists():
            raise serializers.ValidationError('Customer not found!')
        return value
    
    def validate_items(self, items):
        skus = [item['sku'] for item in items]
        found = set(Product.objects.filter(sku__in=skus).values_list('sku',flat=True))
        for item in items:
            if item['sku'] not in found:
                raise serializers.ValidationError(f'Product sku {item['sku']} not found!')
        return items
    
    def create(self, validated_data):
        customer = Customer.objects.get(pk=validated_data['customer_id'])
        items_data = validated_data['items']
        last_orderid = Order.objects.order_by('-orderid').first()
        orderid = last_orderid.orderid + 1 
        order = Order.objects.create(
            orderid = orderid,
            customer = customer,
            ordered = timezone.now(),
            shipped = timezone.now(),
            total = Decimal('0.0')
        )

        total = Decimal('0.0')

        for item in items_data:
            product = Product.objects.get(pk=item['sku'])
            unit_price = product.wholesale_cost
            line_total = unit_price * item['qty']
            OrderItem.objects.create(
                order = order,
                product = product,
                qty= item['qty'],
                unit_price = unit_price,
            )
            total += line_total
        order.total = total
        order.save 
        return order
        