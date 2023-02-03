from rest_framework.routers import DefaultRouter
from product.viewset import ProductViewset, ProductListRetrieveViewset

router = DefaultRouter()
router.register('Product', ProductListRetrieveViewset, basename='product-a')
print(router.urls)
urlpatterns = router.urls

