from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='inicio'),
    path('delete/<int:pk>/', delete, name='eliminar'),
    path('search/<str:name>/', search, name='filter'),
    path('add/<int:pk>/', agregar_producto, name='agregar'),
    path('carrito/', ver_carrito, name='carrito'),
    path('comprar/', comprar, name='comprar'),
    path('cancelar/', cancelar, name='cancelar'),
]