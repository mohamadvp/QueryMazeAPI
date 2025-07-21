from django.db.models.functions import TruncDate
from django.db.models import Sum, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Order


class SalesByDay(APIView):
    def get(self, request):
        start_date = request.query_params.get('start')
        end_date = request.query_params.get('end')

        if not start_date and end_date:
            return Response({"detail": "Provide 'start' and 'end' query params (YYYY-MM-DD)."})

        sales_day = Order.objects.filter(ordered__date__range=[start_date, end_date]).annotate(
            date=TruncDate('ordered')).values('date').annotate(total_count=Count('orderid')).annotate(
                total_spent = Sum('total')
            )

        # serializers = OrderByCustomerSerializers(sales_day, many=True)

        result = [
            {
                'date':item['date'],
                'total_count':item['total_count'],
                'total_spent':item['total_spent']
            }
            for item in sales_day
        ]

        return Response(result)