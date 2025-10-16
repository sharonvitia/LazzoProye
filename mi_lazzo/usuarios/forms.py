from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES, label="Tipo de usuario")
    nombre_completo = forms.CharField(max_length=100, label="Nombre completo")
    email = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = Usuario
        fields = ['username', 'nombre_completo', 'email', 'tipo_usuario', 'password1', 'password2']
