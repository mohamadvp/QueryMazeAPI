from django.db.models import Sum
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.createOrder import OrderCreateSerializer
from ..serializers.orderSerializers import CustomerSerializer,OrderByCustomerSerializers
from ..models import Customer,Order

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

class OrderCreateApiView(APIView):
    def post(self,request):
        serializer= OrderCreateSerializer(data = request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response({
                'order_id':order.orderid,
                'total':order.total,
                'ordered':order.ordered,
                'customer':order.customer.name,
                'item_count':order.orderitem_set.count()
            },status= status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    

