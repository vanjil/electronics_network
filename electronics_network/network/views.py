from rest_framework import viewsets, permissions, filters
from .models import NetworkUnit, Product
from .serializers import NetworkUnitSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from .models import Address
from .serializers import AddressSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

class NetworkUnitViewSet(viewsets.ModelViewSet):
    queryset = NetworkUnit.objects.select_related('address').all()
    serializer_class = NetworkUnitSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['address__country']  # Фильтрация по стране через адрес
    search_fields = ['address__city', 'name']  # Поиск по городу и названию

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('suppliers').all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]