from django.db import models
from usuarios.models import Usuario

class Producto(models.Model):
    emprendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'emprendedor'})
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')
    vendido = models.BooleanField(default=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

