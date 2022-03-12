from django.urls import path
from .views import *

urlpatterns = [
   path('', welcome, name='welcome'),
   path('signin/', signin, name='signin'),
   path('signup/', signup, name='signup'),
   path('masters/', masters, name='masters'),
   path('services/', services, name='services'),
   path('products/', products, name='products'),
   path('success/', success, name='success'),
   path('hub/', hub, name='hub'),
   path('add-master/', add_master, name='add_master'),
   path('add-product/', add_product, name='add_product'),
   path('add-service/', add_service, name='add_service'),
   path('masters/delete-master/<int:id>/', delete_master, name='delete_master'),
   path('products/delete-product/<int:id>/', delete_product, name='delete_product'),
   path('services/delete-service/<int:id>/', delete_service, name='delete_service'),
]
