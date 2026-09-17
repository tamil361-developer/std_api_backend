from django.urls import path
from . import views
app_name = 'myapp'

urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('orders/', views.orders, name='orders'),
    path('order_details/', views.order_details, name='order-details'),
    path('order-details/', views.order_details, name='order-details-hyphenated'),
    path('products/', views.products, name='products'),
]