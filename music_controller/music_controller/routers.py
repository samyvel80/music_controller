from rest_framework.routers import DefaultRouter
from product.viewset import ProductViewset, ProductListRetrieveViewset

router = DefaultRouter()
router.register('ListRetrieve', ProductListRetrieveViewset, basename='ListRetrieve')
router.register('ProductViewset', ProductViewset, basename='Product')
print(router.urls)
urlpatterns = router.urls

