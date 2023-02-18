from rest_framework import serializers
from .models import Product, Category
from api.serializer import UserPublicSerializer
from rest_framework.reverse import reverse
from .validators import validate_unique_name
from django.contrib.auth.models import User






class UserPublicSerializerMethode3(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

class UserPublicSerializerMethode4(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    user_product = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields= ('username', 'id', 'user_product')
    def get_user_product(self,instance): # obj représent une instance de 'user' (regarder source= )
        request = self.context.get('request')
        user = instance
        product = user.product_set.all()
        return ProductInlineserializerMethode4(product, many=True, context={'request':request}).data
class ProductInlineserializerMethode4(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="productdetail", lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()

class ProductInlineserializerMethode5(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="productdetail", lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()

class CategoryInLineSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)





class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="productdetail", lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators=[validate_unique_name])
    #-------------- pour afficher le user Méthode 1---------------------------:
    #user_name = serializers.CharField(source="user.username", read_only=True)

    ##----------------------Sérialization  Méthode 2----------------
    ##owner = serializers.SerializerMethodField(read_only=True)
    ##def get_owner(self, instance):
    ##    return {'username': instance.user.username}
    ## Fin Méthode 2

    ### -------------------- Serialisation Méthode 3 -----------------------------------
    owner = UserPublicSerializerMethode3(source='user', read_only=True)
    cat = CategoryInLineSerializer(source='category', read_only=True)
    #### -------------------- Serialisation Méthode 4 ----------------------------------
    #owner = UserPublicSerializerMethode4(source='user', read_only=True)

    #### -------------------- Serialisation Méthode 5 ----------------------------------
    #owner = ProductInlineserializerMethode5(source='user.product_set.all',many=True)

    class Meta:
        model = Product
        fields = ('owner','cat', 'email', 'url', 'name', 'content', 'price', 'my_discount', 'public')

    def validate_name(self, value):
        request = self.context.get('request')
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

#Méthode open classroom

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
        query_set = user.product_set.all()#la liste des produits d'un utilisateur user.product_set.all() (inverse relation)
        print(query_set)
        return UserProductinLineSerializer(query_set, many=True, context={'request':request}).data

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    prod = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('name','prod')
        def get_prod(self,instance):
            request = self.context.get('request')  # on récupère le request
            qs = instance.product.all()
            return UserProductinLineSerializer(qs, many=True, context={'request':request}).data


class UserProductinLineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="productdetail", lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()
