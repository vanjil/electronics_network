from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkUnitViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'network-units', NetworkUnitViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]