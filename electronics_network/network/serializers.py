from rest_framework import serializers
from .models import NetworkUnit, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'model', 'release_date', 'network_unit']

class NetworkUnitSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = NetworkUnit
        fields = [
            'id', 'name', 'contact_email', 'country', 'city', 'street', 
            'building_number', 'supplier', 'debt', 'created_at', 'products'
        ]
        read_only_fields = ['debt']