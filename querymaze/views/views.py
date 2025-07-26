from django.db.models import Count, Sum, Max, Prefetch, ExpressionWrapper, DecimalField, F
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.serializers import CustomerSerializer, TopCustomerSerializer, OrderReportSerializer, BestSellingProductSerializer
from ..serializers.createOrder import OrderCreateSerializer
from ..models import Customer, Product, Order, OrderItem


class CustomerViewSet(ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.annotate(
            total_number=Count('order'),
            total_spent=Sum('order__total'),
            last_order=Max('order__ordered')
        ).order_by('total_spent')


class BestSellingProduct(ListAPIView):
    serializer_class = BestSellingProductSerializer

    def get_queryset(self):
        revenue_expr = ExpressionWrapper(F('orderitem__qty') * F('orderitem__unit_price'), output_field=DecimalField(max_digits=20, decimal_places=3))
        return Product.objects.annotate(
            total_qty = Sum('orderitem__qty'),
            total_revenue = Sum(revenue_expr)
        ).filter(total_revenue__isnull=False).order_by('-total_revenue')


class OrderReportApiView(ListAPIView):
    serializer_class = OrderReportSerializer

    def get_queryset(self):
        return Order.objects.filter(ordered__range=('2020-01-01', '2021-01-01')).select_related('customer').prefetch_related(
            Prefetch('orderitem_set', queryset=OrderItem.objects.select_related('product')))

# class OrderViewSet(ModelViewSet):
#     queryset = Order.objects.filter(ordered__year='2020').select_related('customer').prefetch_related('orderitem_set')
#     serializer_class = OrderSerializer





