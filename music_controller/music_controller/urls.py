"""music_controller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from product.viewset import ProductViewset
#from product.views import ProViewset
from api.views import RoomViewset
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.SimpleRouter()
router.register('roomViewset', RoomViewset, basename='room')
#router.register('ProViewset', ProViewset, basename='proviewset')
router.register('ProductViewset', ProductViewset, basename='proviewset')
urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('spotify/', include('spotify.urls')),
    path('apiViewset/', include(router.urls)),
    path('product/', include('product.urls')), # Appel de view qui hérite de generics.Retrieve, Create, Update
    path('product/v2/', include('music_controller.routers')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]
