from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

from rest_framework_simplejwt.views import ( 
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from products.views import product_list_create_view


urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', views.api_home, name= "api_home"),

        ########  JWT  ###########s
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('products/', product_list_create_view, name='product-list'),
]
