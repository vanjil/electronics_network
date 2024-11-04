from rest_framework import viewsets, permissions, filters
from .models import NetworkUnit, Product
from .serializers import NetworkUnitSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

class NetworkUnitViewSet(viewsets.ModelViewSet):
    queryset = NetworkUnit.objects.all()
    serializer_class = NetworkUnitSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['country']
    search_fields = ['city', 'name']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
