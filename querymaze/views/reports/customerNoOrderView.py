from rest_framework.generics import ListAPIView
from ...serializers.orderByCustomer import CustomerNoOrderSerializers
from ...models import Customer

class CustomerNoOrdersApiView(ListAPIView):
    serializer_class = CustomerNoOrderSerializers

    def get_queryset(self):
        return Customer.objects.filter(order__isnull=True).prefetch_related('order_set')
