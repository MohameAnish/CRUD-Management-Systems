from django.urls import path
from .views import *
urlpatterns = [
    path('home/', HomePage, name='home'),
    path('services/',ServicesPage, name='services'),
    path('contact/',ContactPage, name='contact'),
    path('about/', AboutPage, name='about'),
    path('product_add/', Product_add, name='product_add'),
    path('product_view/', Product_view, name='product_view'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    path('product_update/<int:id>/', product_update, name='product_update'),
    path('customer_add/', Customer_add, name='customer_add'),
    path('customer_view/', Customer_view, name='customer_view'),
    path('delete_customer/<int:id>/', delete_customer, name='delete_customer'),
    path('customer_update/<int:id>/', customer_update, name='customer_update'),
    path('orders_add/', Orders_add, name='orders_add'),
    path('orders_view/', Orders_view, name='orders_view'),
    path('delete_order/<int:id>/', delete_order, name='delete_order'),
    path('orders_update/<int:id>/', order_update, name='order_update'),]