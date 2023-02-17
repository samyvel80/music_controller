from .models import Product
from .serializers import ProductSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from .authentication import TokenAuthentication
from rest_framework import generics, mixins
#from api.permissions import IsStaffPermission
from api.mixin import StaffEditorPermissionsMixin, UserQuerrySetMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import client
class UserListView(
    StaffEditorPermissionsMixin,
    generics.ListAPIView,
    ):
    queryset = User.objects.all()
    print(queryset)
    serializer_class = UserSerializer


class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ListCreateProductView(
    StaffEditorPermissionsMixin,
    #UserQuerrySetMixin,# surcharge du Queryset pour retourner les produits filtrés par user
    generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #user_field = 'user' # on surcharge le mixin par la valeur 'user'
#   authentication_classes = [authentication.SessionAuthentication]
    #authentication_classes = [authentication.SessionAuthentication, TokenAuthentication] #ajout dans défault settings
    #permission_classes = [permissions.IsAdminUser, IsStaffPermission] #ajouter dans StaffEditorPermissionsMixin
    #IsStaffPermission


    # pour filtrer par user Méthode 1
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        return qs.filter(user=user)

    #def get(self, request, *args, **kwargs):
    #    return self.list(request, *args, **kwargs)
    def perform_create(self, serializer):
        email = serializer.validated_data.pop('email')
        print("view_performcreate")
        print(email)
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content= name
        serializer.save(content=content, user=self.request.user) # user=self.request.user permet d'ajouter le user qui a creer le produit



class SearchListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if not query:
            return Response("Aucun produit trouve")
        result = client.perform_search(query)
        return Response(result)
class SearchOldListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q= self.request.GET.get('q')
        result = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user= self.request.user
                result = qs.search(q,user)
        return result





class UpdateProductView(
    StaffEditorPermissionsMixin,
    UserQuerrySetMixin,
    generics.UpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content= name
        serializer.save(content=content)
class DeleteProductView(
    StaffEditorPermissionsMixin,
    UserQuerrySetMixin,
    generics.DestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #possible de faire un filtre sur le queryset en surchargeant def queryset
    '''
    def get_queryset(self):
        return super().get_queryset().filter(name='Avocat')
    '''
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
        #méthode get est identique pour list et retrieve
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

class ProViewset(viewsets.ModelViewSet):
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

'''
@api_view(['GET','POST'])
def api_view(request, *args, **kwargs):
    if request.method != "POST"
        return Response({"detail:method not allowed"})
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
        #data = model_to_dict(query, fields=('name', 'content', 'price', 'get_discount'))
        serializer = ProductSerializer(query)
        data = serializer.data
         #Response => Serialise les donnees dict-> en Json
    return Response(data)

@api_view(['GET'])
def api_view(request, *args, **kwargs):
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
        #data = model_to_dict(query, fields=('name', 'content', 'price', 'get_discount'))
        serializer = ProductSerializer(query)
        data = serializer.data
         #Response => Serialise les donnees dict-> en Json
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