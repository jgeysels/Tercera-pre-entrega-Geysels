from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def detalle_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})

def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'nuevo_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('detalle_cliente', id=cliente.id)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'eliminar_cliente.html', {'cliente': cliente})




