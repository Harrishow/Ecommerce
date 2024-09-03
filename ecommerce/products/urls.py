from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('products_v2/<int:pk>/', views.product_detail_v2, name='product-detail_v2'),
]
