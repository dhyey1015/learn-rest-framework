from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view),
    path('', views.product_list_create_view),
    path('<int:pk>/', views.ProductListCreateAPIView.as_view()),
    ########3 class view functions
    path('create/', views.product_list_create_view, name="product_create"),
    path('<int:pk>/detail/', views.ProductDetailAPIView.as_view(), name="product_detail"),
    path('list/', views.product_list_create_view, name="product_list"),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name="product_edit"),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view(), name="product_delete"),

    path('mixins/', views.ProductMixinsView.as_view()),
    path('<int:pk>/mixins/', views.ProductMixinsView.as_view()),
]

