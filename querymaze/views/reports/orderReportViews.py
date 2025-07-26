from django.db.models import Prefetch
from rest_framework.generics import ListAPIView
from ...serializers.reportSerializers import OrderReportSerializer
from ...models import Order, OrderItem

class OrderReportApiView(ListAPIView):
    serializer_class = OrderReportSerializer

    def get_queryset(self):
        return Order.objects.filter(ordered__range=('2020-01-01', '2021-01-01')).select_related('customer').prefetch_related(
            Prefetch('orderitem_set', queryset=OrderItem.objects.select_related('product')))