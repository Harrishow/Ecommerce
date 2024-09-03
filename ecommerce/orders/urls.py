from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer-list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer-detail'),
    path('orders/', views.order_list, name='order-list'),
    path('orders_v2/<int:pk>/', views.order_detail_v2, name='order-detail_v2'),
]
