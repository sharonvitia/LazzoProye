from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        ('emprendedor', 'Emprendedor'),
        ('consumidor', 'Consumidor'),
    )
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    nombre_completo = models.CharField(max_length=100)
    # Email y contraseña ya vienen de AbstractUser

    def __str__(self):
        return self.username

class Tarjeta(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'consumidor'})
    numero_tarjeta = models.CharField(max_length=16)
    fecha_expiracion = models.CharField(max_length=5)
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return f"Tarjeta de {self.usuario.username}"

