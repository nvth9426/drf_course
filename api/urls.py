from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
  # path('products/', views.product_list, name='products'),
  # path('products/<int:pk>/', views.product_detail, name='product_detail'),
  path('products/', views.ProductListAPIView.as_view()),
  # path('products/create/', views.ProductCreateAPIView.as_view()),
  path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
  # path('products/info/', views.product_info, name='product_info'),
  path('products/info/', views.ProductInfoAPIView.as_view(), name='product_info'),
  # path('orders/', views.order_list, name='orders'),
  
  # path('orders/', views.OrdertListAPIView.as_view()),
  # path('user-orders/', views.UserOrdertListAPIView.as_view(), name='user-orders'),
]

router = DefaultRouter()
router.register('orders', views.OrderViewSet)
urlpatterns += router.urls