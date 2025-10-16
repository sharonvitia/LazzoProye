from django.db import models
from usuarios.models import Usuario
from productos.models import Producto

class CarritoItem(models.Model):
    consumidor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'consumidor'})
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Compra(models.Model):
    consumidor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(CarritoItem)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    pagado = models.BooleanField(default=False)

