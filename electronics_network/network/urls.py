from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkUnitViewSet, ProductViewSet, AddressViewSet

router = DefaultRouter()
router.register(r'network-units', NetworkUnitViewSet)
router.register(r'products', ProductViewSet)
router.register(r'addresses', AddressViewSet)  # добавлен маршрут для Address


urlpatterns = [
    path('', include(router.urls)),
]