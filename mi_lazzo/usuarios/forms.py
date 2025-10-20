"""from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES, label="Tipo de usuario")
    nombre_completo = forms.CharField(max_length=100, label="Nombre completo")
    email = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = Usuario
        fields = ['username', 'nombre_completo', 'email', 'tipo_usuario', 'password1', 'password2']"""
        
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroForm(UserCreationForm):
    """Formulario base de registro"""
    tipo_usuario = forms.ChoiceField(
        choices=Usuario.TIPO_USUARIO_CHOICES,
        label="Tipo de usuario",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    nombre_completo = forms.CharField(
        max_length=100,
        label="Nombre completo",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre completo'})
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'})
    )

    class Meta:
        model = Usuario
        fields = ['username', 'nombre_completo', 'email', 'tipo_usuario', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmar contraseña'})


class RegistroEmprendedorForm(UserCreationForm):
    """Formulario específico para registro de emprendedores"""
    nombre_completo = forms.CharField(
        max_length=100,
        label="Nombre completo",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre completo'
        })
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        })
    )
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Elige un nombre de usuario único'
        })
    )

    class Meta:
        model = Usuario
        fields = ['username', 'nombre_completo', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Mínimo 8 caracteres'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña'
        })
        
        # Personalizar labels
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"


class RegistroConsumidorForm(UserCreationForm):
    """Formulario específico para registro de consumidores"""
    nombre_completo = forms.CharField(
        max_length=100,
        label="Nombre completo",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre completo'
        })
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        })
    )
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Elige un nombre de usuario único'
        })
    )

    class Meta:
        model = Usuario
        fields = ['username', 'nombre_completo', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Mínimo 8 caracteres'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña'
        })
        
        # Personalizar labels
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
