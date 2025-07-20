
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.createOrder import OrderCreateSerializer

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