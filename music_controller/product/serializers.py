from rest_framework import serializers
from .models import Product
from api.serializer import UserPublicSerializer
from rest_framework.reverse import reverse
from .validators import validate_unique_name
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    product = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ('username', 'id', 'product')
    def get_product(self,obj):
        request = self.context.get('request') # on récupère le request
        user = obj
        query_set = obj.product_set.all()#la liste des produits d'un utilisateur user.product_set.all() (inverse relation)
        print(query_set)
        return UserProductinLineSerializer(query_set, many=True, context={'request':request}).data


class UserProductinLineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="productdetail", lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="productdetail", lookup_field='pk')
    #owner = UserPublicSerializer(source= 'user', read_only=True)
    #owner = UserProductinLineSerializer(source='user.product_set.all', many=True, read_only=True)# on entre dans source la Foreign KEY
    email= serializers.EmailField(write_only=True)
    name = serializers.CharField(validators=[validate_unique_name])


    class Meta:
        model = Product
        fields = ('email', 'url', 'name', 'content', 'price', 'my_discount')

    def validate_name(self, value):
        request= self.context.get('request')
        qs = Product.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"la produit {value} existé déjà")
        return value



    '''
      #owner = serializers.SerializerMethodField(read_only=True)
       #owner = UserProductInlineSerialier(source= 'user.product_set.all',many=True, read_only=True)
    #owner = UserPublicSerializer(source= 'user', read_only=True)
      #url = serializers.SerializerMethodField(read_only=True)
    #user_name = serializers.CharField(source="user.username", read_only=True)#8h58 dans tuto, on bloque l'apparition du champ dans create
    #name = serializers.CharField(validators=[validate_unique_name])
    def create(self, validated_data):
        print(validated_data)
        email = validated_data.pop('email')
        print(email)
        print(validated_data)
        #return Product.objects.create(**validated_data)
        obj = super().create(validated_data)
        return obj
    '''
    def update(self, instance, validated_data):
        print("view_performUpdate")
        print(validated_data)
        email = validated_data.pop('email')
        print(validated_data)
        print(email)
        #instance.name = validated_data.get('name')
        return super().update(instance, validated_data)
    #def get_url(self, obj):
    #    request = self.context.get('request')
    #    if request is None:
    #        return None
    #    return reverse("productdetail", kwargs={'pk':obj.pk}, request=request)
        #return f"/product/{obj.pk}/detailMixin"
    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount
    #def get_owner(self,obj):
    #    return {'username': obj.user.username, 'id':obj.user.pk}