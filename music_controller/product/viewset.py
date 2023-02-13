from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets,mixins
from api.mixin import StaffEditorPermissionsMixin

class ProductViewset(viewsets.ModelViewSet):
    """
    get -> list -> Queryset
    get -> retrieve
    post -> create
    put -> update
    patch -> partial update
    delete -> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListRetrieveViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer