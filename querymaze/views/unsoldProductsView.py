from rest_framework.generics import ListAPIView
from ..serializers.serializers import ProductSerializer
from ..models import Product

class UnsoldProductView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(orderitem__isnull=True)