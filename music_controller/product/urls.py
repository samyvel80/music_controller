from django.urls import path, include
from .views import DetailProductView, CreateProductView, UpdateProductView
#from .views import api_view
urlpatterns = [

    #path('', api_view, name='api_view'),
    path('<int:pk>/', DetailProductView.as_view() ),
    path('create/', CreateProductView.as_view()),
    path('<int:pk>/update/', UpdateProductView.as_view()),
    ]

