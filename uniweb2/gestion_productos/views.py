from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto
from .forms import ProductoForm


def home(request):
    return render(request, 'gestion_productos/home.html')


def guardar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'gestion_productos/registro_producto.html', {'form': form})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestion_productos/lista_productos.html', {'productos': productos})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'gestion_productos/editar_producto.html', {'form': form, 'producto': producto})


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    # GET: mostrar página de confirmación
    return render(request, 'gestion_productos/confirmar_eliminar.html', {'producto': producto})
