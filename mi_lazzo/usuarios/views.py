from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import login

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Inicia sesión automáticamente después del registro
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})



def inicio(request):
    return render(request, 'usuarios/inicio.html')
