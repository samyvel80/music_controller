from rest_framework import serializers
from product.models import Product
from django.contrib.auth.models import User
class ProductinLineSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="productdetail", lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()
    class Meta:
        model = Product
        fields = ('url','email', 'name')

class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    user_product = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields= ('username', 'id', 'user_product')
    def get_user_product(self,obj):
        request = self.context.get('request') # on récupère le request
        user = obj
        product = user.product_set.all()#la liste des produits d'un utilisateur user.product_set.all() (inverse relation)

        return ProductinLineSerializer(product, many=True, context={'request':request}).data
'''
class ProductInlineSerialier(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="productdetail", lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()


class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    has_perm = serializers.BooleanField(read_only=True)
    user_product = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields= ('username', 'id', 'has_perm', 'user_product')
    def get_user_product(self,obj):
        user = obj
        request = self.context.get('request')
        product = user.product_set.all()[:3]# user.product_set.all()
        return ProductInlineSerialier(product, many=True, context={'request':request}).data
'''