from rest_framework import permissions

class IsStaffPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)
    #permet de bloquer l'accès à la création quand acces à liste uniquement
    # il faut ajouter '%(app_label)s.view_%(model_name)s' dans GET pour bloquer l'accès en lecture
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        #'GET':[],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
# Def Has permission est insuffisant : un membre staff avec l'unique autorisation pour voir peut aussi créer un produit
# ListCreateAPIView hérite de plusieurs mixin dant perms_map
''' def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            if user.has_perm('product.add_product') #appname.perm_name_model_name
                return True
            if user.has_perm('product.change_product') #appname.perm_name_model_name
                return True
            if user.has_perm('product.delete_product') #appname.perm_name_model_name
                return True
            if user.has_perm('product.view_product') #appname.perm_name_model_name
                return True
        return False:
'''