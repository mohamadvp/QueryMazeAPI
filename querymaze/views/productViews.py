from django.db.models import ExpressionWrapper, Sum, DecimalField, F
from rest_framework.generics import ListAPIView
from ..serializers.productSerializers import ProductSerializer, BestSellingProductSerializer
from ..models import Product

class UnsoldProductApiView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(orderitem__isnull=True)
    
class BestSellingProductApiView(ListAPIView):
    serializer_class = BestSellingProductSerializer

    def get_queryset(self):
        revenue_expr = ExpressionWrapper(F('orderitem__qty') * F('orderitem__unit_price'), output_field=DecimalField(max_digits=20, decimal_places=3))
        return Product.objects.annotate(
            total_qty = Sum('orderitem__qty'),
            total_revenue = Sum(revenue_expr)
        ).filter(total_revenue__isnull=False).order_by('-total_revenue')