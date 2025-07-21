from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum
from ..serializers.orderByCustomer import CustomerSerializer,OrderByCustomerSerializers
from ..models import Customer, Order

class OrderByCustomerApiView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['get'])
    def orders(self, request, pk=None):
        customer = self.get_object()
        orders = Order.objects.filter(customer=customer).select_related('customer')
        total_orders = orders.count()
        total_spent = Order.objects.filter(customer = customer).aggregate(Sum('total'))

        serializer = OrderByCustomerSerializers(orders, many=True)

        return Response({
            "customer_id": customer.customerid,
            "customer_name": customer.name,
            "total_orders": total_orders,
            "total_spent":total_spent,
            "orders": serializer.data
        })