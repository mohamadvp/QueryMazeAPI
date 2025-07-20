from django.db.models import Sum
from rest_framework.generics import ListAPIView
from ..serializers.topCustomer import TopCustomerSerializers
from ..models import Customer

class TopCustomerApiView(ListAPIView):
    serializer_class = TopCustomerSerializers

    def get_queryset(self):
        return Customer.objects.annotate(
            total_spent = Sum('order__total')
        ).filter(total_spent__isnull = False).order_by('-total_spent')