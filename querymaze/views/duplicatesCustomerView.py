from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q, Count
from collections import defaultdict
from ..serializers.orderByCustomer import CustomerSerializer
from ..models import Customer


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