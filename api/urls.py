from django.urls import path
from . import views


urlpatterns = [
  # path('products/', views.product_list, name='products'),
  # path('products/<int:pk>/', views.product_detail, name='product_detail'),
  path('products/', views.ProductListAPIView.as_view()),
  path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
  path('products/info/', views.product_info, name='product_info'),
  # path('orders/', views.order_list, name='orders'),
  path('orders/', views.OrdertListAPIView.as_view()),
  path('user-orders/', views.UserOrdertListAPIView.as_view(), name='user-orders'),
]