from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from ..serializers.serializers import MiniCustomerSerializer
from ..models import Customer, Order


class DeleteCustomerApiView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = MiniCustomerSerializer

    @action(detail=True, methods=['post'], url_path='delete-customer')
    def delete_customer(self, request, pk=None):
        customer = self.get_object()
        orders = customer.order_set.all()

        for order in orders:
            order.orderitem_set.all().delete()
            order.delete()

        customer.delete()

        return Response({f"message": "Customer and all related orders and order items were deleted."},status=status.HTTP_200_OK)

