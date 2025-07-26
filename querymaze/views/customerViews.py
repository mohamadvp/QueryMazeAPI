from django.db.models import Q, Count, Sum, Max
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from collections import defaultdict
from ..serializers.customerSerializers import CustomerSerializer, CustomerModelSerializer
from ..models import Customer

class CustomerApiView(ListAPIView):
    serializer_class = CustomerModelSerializer

    def get_queryset(self):
        return Customer.objects.annotate(
            total_number=Count('order'),
            total_spent=Sum('order__total'),
            last_order=Max('order__ordered')
        ).order_by('total_spent')

class DeleteCustomerApiView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['post'], url_path='delete-customer')
    def delete_customer(self, request, pk=None):
        customer = self.get_object()
        orders = customer.order_set.all()

        for order in orders:
            order.orderitem_set.all().delete()
            order.delete()

        customer.delete()

        return Response({f"message": "Customer and all related orders and order items were deleted."},status=status.HTTP_200_OK)
    

class DuplicatesCustomerApiView(APIView):
    def get(self, request):
        duplicates = Customer.objects.values('name', 'phone').annotate(
            count=Count('customerid')).filter(count__gt=1)

        query = Q()
        for dup in duplicates:
            query |= Q(name=dup['name'], phone=dup['phone'])

        customers = Customer.objects.filter(query).order_by('name', 'phone')

        grouped = defaultdict(list)
        for customer in customers:
            key = (customer.name, customer.phone)
            grouped[key].append({
                'citystatezip': customer.citystatezip
            })

        result = [
            {
                'name': name,
                'phone': phone,
                'duplicates': duplicates
            }
            for (name, phone), duplicates in grouped.items()
        ]

        return Response(result)