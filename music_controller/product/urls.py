from django.urls import path, include
from .views import DetailProductView, ListCreateProductView, UpdateProductView, DeleteProductView, ListProductView
#from .views import api_view
urlpatterns = [
    #path('', api_view, name='api_view'),
    path('<int:pk>/', DetailProductView.as_view() ),
    #path('create/', CreateProductView.as_view()),
    path('<int:pk>/update/', UpdateProductView.as_view()),
    path('<int:pk>/delete/', DeleteProductView.as_view()),
    path('list/', ListProductView.as_view()),
    path('create-list/', ListCreateProductView.as_view()),
    #path('<int:pk>/detail', ProductMixinsView.as_view()),
    #path('<int:pk>/update', ProductMixinsView.as_view()),
    #path('<int:pk>/delete', ProductMixinsView.as_view()),
    #path('list/', ProductMixinsView.as_view()),


    ]

