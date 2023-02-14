from .permissions import IsStaffPermission
from rest_framework import permissions
class StaffEditorPermissionsMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffPermission] # IsStaffPermission est une classe permission spécifique dans le fichier api.permission

class UserQuerrySetMixin():
    user_field = 'user'
    def get_queryset(self,*args, **kwargs):
        user = self.request.user
        qs = super().get_queryset(*args,**kwargs)
        query_data = {}
        query_data[self.user_field] = self.request.user
        return qs.filter(**query_data) # {'user:'donald'} --> qs.filter(user=donald)
