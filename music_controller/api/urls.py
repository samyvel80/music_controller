from django.urls import path, include
from .views import RoomViewset, RoomView, RoomViewCreate,api_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('room/', RoomView.as_view()),
    path('createroom/', RoomViewCreate.as_view()),
    path('', api_view, name='api_view'),
    path('auth', obtain_auth_token),
    ]
