from rest_framework import serializers
from ..models import Customer

class CustomerModelSerializer(serializers.ModelSerializer):
    total_number = serializers.IntegerField()
    total_spent  = serializers.DecimalField(max_digits=20 , decimal_places=3)
    last_order = serializers.DateTimeField()
    class Meta:
        model = Customer
        fields = ['customerid','name','phone','birthdate','total_number','total_spent','last_order']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','phone']