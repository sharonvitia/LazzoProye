from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto
from usuarios.models import Usuario


def productos_publicos(request):
    """Vista pública de productos para invitados"""
    productos = Producto.objects.filter(vendido=False)
    context = {
        'productos': productos,
    }
    return render(request, 'productos/lista_publica.html', context)


@login_required
def publicar_producto(request):
    """Vista para que emprendedores publiquen productos"""
    # Verificar que el usuario sea emprendedor
    if request.user.tipo_usuario != 'emprendedor':
        messages.error(request, 'Solo los emprendedores pueden publicar productos.')
        return redirect('home_consumidor')
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        imagen = request.FILES.get('imagen')
        
        # Validaciones básicas
        if not all([titulo, descripcion, precio, cantidad]):
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'productos/publicar.html')
        
        try:
            producto = Producto.objects.create(
                emprendedor=request.user,
                titulo=titulo,
                descripcion=descripcion,
                precio=float(precio),
                cantidad=int(cantidad),
                imagen=imagen
            )
            messages.success(request, '¡Producto publicado exitosamente!')
            return redirect('mis_productos')
        except ValueError:
            messages.error(request, 'Por favor verifica que el precio y cantidad sean números válidos.')
            return render(request, 'productos/publicar.html')
    
    return render(request, 'productos/publicar.html')


@login_required
def mis_productos(request):
    """Vista para que emprendedores vean sus productos"""
    if request.user.tipo_usuario != 'emprendedor':
        messages.error(request, 'Acceso denegado.')
        return redirect('home_consumidor')
    
    productos = Producto.objects.filter(emprendedor=request.user).order_by('-fecha_publicacion')
    context = {
        'productos': productos,
    }
    return render(request, 'productos/mis_productos.html', context)


@login_required
def editar_producto(request, producto_id):
    """Vista para editar un producto"""
    producto = get_object_or_404(Producto, id=producto_id, emprendedor=request.user)
    
    if request.method == 'POST':
        producto.titulo = request.POST.get('titulo')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.cantidad = request.POST.get('cantidad')
        
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        
        producto.save()
        messages.success(request, 'Producto actualizado correctamente.')
        return redirect('mis_productos')
    
    context = {
        'producto': producto,
    }
    return render(request, 'productos/editar.html', context)


@login_required
def eliminar_producto(request, producto_id):
    """Vista para eliminar un producto"""
    producto = get_object_or_404(Producto, id=producto_id, emprendedor=request.user)
    
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('mis_productos')
    
    context = {
        'producto': producto,
    }
    return render(request, 'productos/confirmar_eliminar.html', context)


@login_required
def detalle_producto(request, producto_id):
    """Vista detallada de un producto"""
    producto = get_object_or_404(Producto, id=producto_id)
    
    context = {
        'producto': producto,
    }
    return render(request, 'productos/detalle.html', context)


@login_required
def buscar_productos(request):
    """Vista para buscar productos"""
    query = request.GET.get('q', '')
    
    if query:
        productos = Producto.objects.filter(
            titulo__icontains=query,
            vendido=False
        ) | Producto.objects.filter(
            descripcion__icontains=query,
            vendido=False
        )
    else:
        productos = Producto.objects.filter(vendido=False)
    
    context = {
        'productos': productos,
        'query': query,
    }
    return render(request, 'productos/buscar.html', context)