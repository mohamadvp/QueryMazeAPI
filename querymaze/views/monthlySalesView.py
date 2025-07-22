from django.db.models.functions import TruncDate
from django.db.models import ExpressionWrapper, Sum, F, DecimalField, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .. models import OrderItem
from datetime import datetime
import calendar


class MonthlySales(APIView):
    def get(self,request):
        year = int(request.query_params.get('year'))
        start_month = int(request.query_params.get('start'))
        end_month = int(request.query_params.get('end') )

        rev_ex=ExpressionWrapper(F('qty') * F('unit_price'),output_field=DecimalField(max_digits=20, decimal_places=3))

        start_date = datetime(year,start_month,1)
        end_day = calendar.monthrange(year,end_month)[1]
        end_date= datetime(year,end_month,end_day,23,59,59)

        queryset = OrderItem.objects.annotate(
            revenue=rev_ex,
            year=F('order__ordered__year'),
            month=F('order__ordered__month')
        )

        if start_date and end_date:
            queryset = queryset.filter(order__ordered__range=(start_date, end_date))

        grouped = queryset.values('year', 'month').annotate(
            orders=Count('order', distinct=True),
            revenue=Sum('revenue')
        ).order_by('year', 'month')

        result = [
            {
                "month": f"{item['year']}-{item['month']:02}",
                "orders": item['orders'],
                "revenue": float(item['revenue'])
            }
            for item in grouped
        ]

        return Response(result)