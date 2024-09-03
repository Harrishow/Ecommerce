from rest_framework import serializers
from .models import Product

class ProductDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category_name', 'tags']
