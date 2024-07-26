
from django.urls import path
from .views import list_products,cliente_venta
urlpatterns = [
    path('products/', list_products, name='list_products'),
    path('venta/', cliente_venta, name='cliente_venta'),

]