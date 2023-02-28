from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('buscar/', views.buscar, name='buscar'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('lista_ordenes/', views.lista_ordenes, name='lista_ordenes'),
]