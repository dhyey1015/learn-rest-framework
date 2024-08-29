from django.urls import path
from . import views

urlpatterns = [
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view),
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductListCreateAPIView.as_view()),
    ########3 class view functions
    path('create/', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/detail/', views.ProductDetailAPIView.as_view()),
    path('list/', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),
    ##### mixins generic views##########3
    path('mixins/', views.ProductMixinsView.as_view()),
    path('<int:pk>/mixins/', views.ProductMixinsView.as_view()),
]

