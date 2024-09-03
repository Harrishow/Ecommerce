from rest_framework import serializers
from .models import Order

class OrderDetailSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.first_name', read_only=True)
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'date_ordered', 'items']
