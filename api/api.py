from products import views as product_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', product_views.ProductViewSet, basename='products')
