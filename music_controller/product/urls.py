from django.urls import path, include
from .views import DetailProductView, ListCreateProductView, UpdateProductView, DeleteProductView, ListProductView, ProductMixinsView, SearchListView, UserListView
#from .views import api_view
urlpatterns = [
    #path('', api_view, name='api_view'),
    path('list/', ListProductView.as_view()),
    path('<int:pk>/', DetailProductView.as_view() ),

    #path('create/', CreateProductView.as_view()),
    path('<int:pk>/update/', UpdateProductView.as_view(),name='update'),
    path('<int:pk>/delete/', DeleteProductView.as_view()),
    path('user-list/', UserListView.as_view()),
    path('create-list/', ListCreateProductView.as_view()),
    path('search/', SearchListView.as_view()),
   # path('listMixin/', ProductMixinsView.as_view()), #get      #get
    path('<int:pk>/detailMixin', ProductMixinsView.as_view(),name='productdetail'), #get
   # path('createMixin/', ProductMixinsView.as_view()),         #post
   # path('<int:pk>/updateMixin', ProductMixinsView.as_view()), #put
   # path('<int:pk>/deleteMixin', ProductMixinsView.as_view()), #delete



    ]

