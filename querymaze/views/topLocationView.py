from django.db.models import Count, ExpressionWrapper, F, Sum, DecimalField
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Customer, OrderItem


class TopLocationApiView(APIView):
    def get(self, request):

        rev_ex = ExpressionWrapper(F('order__orderitem__qty') * F(
            'order__orderitem__unit_price'), output_field=DecimalField(max_digits=20, decimal_places=3))
         

        customers = Customer.objects.values('citystatezip').annotate(
            count=Count('customerid',distinct=True),
            revenue=Sum(rev_ex),
            total_order = Count('order',distinct=True)
        ).filter(revenue__isnull=False).order_by('-revenue')

        result = [
            {
                'location': customer['citystatezip'],
                'customers': customer['count'],
                'revenue': customer['revenue'],
                'avrage': round(customer['revenue'] / customer['total_order'],2) if customer['total_order'] else 0
            }
            for customer in customers
        ]

        return Response(result)
