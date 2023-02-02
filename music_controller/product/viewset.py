from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets

class ProductViewset(viewsets.ModelViewSet):
    """
    get -> list -> Queryset
    get -> retrieve
    post -> create
    put -> update
    patch -> partial update
    delete -> destroy
    """
    queryset = Product.object.all()
    serializer_class = ProductSerializer