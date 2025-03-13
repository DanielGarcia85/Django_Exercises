from django.urls import path, include
from .views import order_list
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # URL pour accéder aux API
    path('api-auth/', include('rest_framework.urls')),  # Permet la connexion via l'interface DRF
]