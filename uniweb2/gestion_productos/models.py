from django.db import models

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.nombre_producto
# Create your models here.
