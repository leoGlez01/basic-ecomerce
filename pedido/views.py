from django.shortcuts import get_object_or_404, render, redirect
from producto.models import Producto
from .models import *
from django.db.models import Q


def home(request):
    """View function for home page of site."""
    producto = Producto.objects.all()
    return render(request, "home.html", context={"productos": producto})


def search(request, name):
    producto = Producto.objects.filter(
        Q(nombre__startswith=name)
    )
    if len(producto) >= 0:
        context = {"producto": producto}
        return render(request, "home.html", context=context)
    else:
        context = {}
        return render(request, "home.html", context=context)


def delete(request, pk):
    ElementoCarrito.objects.filter(id=pk).delete()
    return redirect("carrito")


def agregar_producto(request, pk):
    producto = get_object_or_404(Producto, id=pk)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    elemento_carrito, creado = ElementoCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not creado:
        elemento_carrito.cantidad += 1
        elemento_carrito.save()
    return redirect('carrito')


def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    elementos_carrito = carrito.elementocarrito_set.all()
    return render(request, 'carrito.html', {'elementos_carrito': elementos_carrito})

from typing import Dict

def comprar(request):
    if request.method == 'POST':
        carrito = request.session.get('carrito', {})
        for id, cantidad in carrito.items():
            producto = Producto.objects.get(id=id)
            producto.cantidad -= cantidad
            producto.save()
            carrito[id] = 0  # set the quantity to 0 instead of removing the item
        request.session['carrito'] = {}  # clear the entire carrito session
    return redirect('inicio')

def cancelar(request):
    if request.method == 'POST':
        request.session['carrito'] = {}  # clear the entire carrito session
    return redirect('inicio')