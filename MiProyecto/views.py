from django.shortcuts import render, redirect
from .models import Cliente, Producto, Orden
from .forms import ClienteForm


def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def buscar(request):
    if 'query' in request.GET:
        query = request.GET['query']
        clientes = Cliente.objects.filter(nombre__icontains=query)
        productos = Producto.objects.filter(nombre__icontains=query)
        ordenes = Orden.objects.filter(cliente__nombre__icontains=query)
    else:
        clientes = []
        productos = []
        ordenes = []
    return render(request, 'buscar.html', {'clientes': clientes, 'productos': productos, 'ordenes': ordenes})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def lista_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'lista_ordenes.html', {'ordenes': ordenes})

def index(request):
    return render(request, 'index.html')



