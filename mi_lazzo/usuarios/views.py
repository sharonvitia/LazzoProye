"""from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Inicia sesión automáticamente después del registro
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})
    
def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            if usuario.tipo_usuario == 'emprendedor':
                return redirect('home_emprendedor')
            else:
                return redirect('home_consumidor')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})



def inicio(request):
    return render(request, 'usuarios/inicio.html')

@login_required
def home_view(request):
    return render(request, 'usuarios/home.html')

@login_required
def home_emprendedor(request):
    # Lógica para productos del emprendedor
    productos = Producto.objects.filter(emprendedor=request.user)
    return render(request, 'usuarios/perfil_emprendedor.html', {'productos': productos})

@login_required
def home_consumidor(request):
    # Lógica para carrito o productos
    return render(request, 'usuarios/perfil_consumidor.html')"""
    
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm, RegistroEmprendedorForm, RegistroConsumidorForm
from .models import Usuario
from productos.models import Producto


def inicio(request):
    """Página de inicio/bienvenida"""
    if request.user.is_authenticated:
        if request.user.tipo_usuario == 'emprendedor':
            return redirect('home_emprendedor')
        else:
            return redirect('home_consumidor')
    return render(request, 'usuarios/inicio.html')


def seleccion_tipo_usuario(request):
    """Pantalla para seleccionar tipo de usuario"""
    return render(request, 'usuarios/seleccion_tipo.html')


def registro_emprendedor(request):
    """Registro específico para emprendedores"""
    if request.method == 'POST':
        form = RegistroEmprendedorForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.tipo_usuario = 'emprendedor'
            usuario.save()
            login(request, usuario)
            messages.success(request, '¡Registro exitoso! Bienvenido a Lazzo.')
            return redirect('home_emprendedor')
    else:
        form = RegistroEmprendedorForm()
    return render(request, 'usuarios/registro_emprendedor.html', {'form': form})


def registro_consumidor(request):
    """Registro específico para consumidores"""
    if request.method == 'POST':
        form = RegistroConsumidorForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.tipo_usuario = 'consumidor'
            usuario.save()
            login(request, usuario)
            messages.success(request, '¡Registro exitoso! Bienvenido a Lazzo.')
            return redirect('home_consumidor')
    else:
        form = RegistroConsumidorForm()
    return render(request, 'usuarios/registro_consumidor.html', {'form': form})


def login_view(request):
    """Vista de login"""
    if request.user.is_authenticated:
        return redirect('inicio')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido de nuevo, {user.nombre_completo}!')
            
            if user.tipo_usuario == 'emprendedor':
                return redirect('home_emprendedor')
            else:
                return redirect('home_consumidor')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'usuarios/login.html')


def logout_view(request):
    """Vista de logout"""
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('inicio')


def invitado_view(request):
    """Vista para continuar como invitado"""
    # Aquí puedes mostrar productos sin necesidad de login
    # o redirigir a una vista pública
    return redirect('productos_publicos')


@login_required
def home_view(request):
    """Home general - redirige según tipo de usuario"""
    if request.user.tipo_usuario == 'emprendedor':
        return redirect('home_emprendedor')
    else:
        return redirect('home_consumidor')


@login_required
def home_emprendedor(request):
    """Dashboard para emprendedores"""
    productos = Producto.objects.filter(emprendedor=request.user)
    context = {
        'productos': productos,
        'total_productos': productos.count(),
        'productos_vendidos': productos.filter(vendido=True).count(),
    }
    return render(request, 'usuarios/perfil_emprendedor.html', context)


@login_required
def home_consumidor(request):
    """Dashboard para consumidores"""
    # Obtener todos los productos disponibles
    productos = Producto.objects.filter(vendido=False)
    context = {
        'productos': productos,
    }
    return render(request, 'usuarios/perfil_consumidor.html', context)