from rest_framework import serializers
from querymaze.models import Customer

class TopCustomerSerializers(serializers.ModelSerializer):
    total_spent = serializers.DecimalField(max_digits=20 , decimal_places=3, read_only = True)
    class Meta:
        model = Customer
        fields = ['customerid','name','phone','total_spent']