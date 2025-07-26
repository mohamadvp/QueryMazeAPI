from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...serializers.reportSerializers import TopCustomerSerializers
from ...models import Customer

class TopCustomerByCity(APIView):
    
    def get(self, request):
        city = request.query_params.get('city')

        if not city:
            return Response(f'There is no such a city',status=status.HTTP_404_NOT_FOUND)
        
        queryset = Customer.objects.filter(citystatezip__icontains=city).annotate(
            total_spent = Sum('order__total')
        ).filter(total_spent__isnull=False).order_by('-total_spent')

        serializer = TopCustomerSerializers(queryset , many=True)

        return Response(serializer.data)

