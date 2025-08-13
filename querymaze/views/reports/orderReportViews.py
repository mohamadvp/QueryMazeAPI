from django.db.models import Prefetch
from rest_framework.views import APIView
from rest_framework.response import Response
from ...serializers.reportSerializers import OrderReportSerializer
from ...models import Order, OrderItem


class OrderReportApiView(APIView):

    def get(self, request):
        start_data = request.query_params.get('start')
        end_date = request.query_params.get('end')

        queryset = Order.objects.filter(ordered__date__range=[start_data,end_date]).select_related('customer').prefetch_related(
            Prefetch('orderitem_set', queryset=OrderItem.objects.select_related('product')))
        
        serializer = OrderReportSerializer(queryset, many=True)

        return Response(serializer.data)
