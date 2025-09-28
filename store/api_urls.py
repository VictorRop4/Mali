from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, CheckoutView,  ReviewViewSet, OrderViewSet
from django.urls import path, include
from .views import mpesa_callback

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

router.register(r'orders', OrderViewSet, basename='order')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path("", include(router.urls)),  # include viewsets
    path("checkout/", CheckoutView.as_view(), name="checkout"),
   
]
