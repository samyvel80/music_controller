from .models import Product
from .serializers import ProductSerializer
from .authentication import TokenAuthentication
from rest_framework import generics, mixins,permissions
from api.permissions import IsStaffPermission

#if __name__ == '__main__':
#from music_controller.api.mixin import StaffEditorPermissionsMixin

class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListCreateProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
#   authentication_classes = [authentication.SessionAuthentication]
    #authentication_classes = [authentication.SessionAuthentication, TokenAuthentication] #ajout dans default settings
    permission_classes = [permissions.IsAdminUser, IsStaffPermission] #ajouter dans StaffEditorPermissionsMixin
    #IsStaffPermission
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content= name
        serializer.save(content=content)
class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content= name
        serializer.save(content=content)
class DeleteProductView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        return super().get_queryset()

class ProductMixinsView(
        generics.GenericAPIView, #post
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,# put
        mixins.ListModelMixin,#get
        mixins.DestroyModelMixin,
        mixins.RetrieveModelMixin): #get

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content= name
        serializer.save(content=content)
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content= name
        serializer.save(content=content)
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
'''
@api_view(['GET'])
def api_view(request, *args, **kwargs):
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
        #data = model_to_dict(query, fields=('name', 'content', 'price', 'get_discount'))
        serializer = ProductSerializer(query)
        data = serializer.data
        # Response => Serialise les donnees dict-> en Json
    return Response(data)

@api_view(['POST'])
def api_view(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'detail': 'invalid data'})
'''