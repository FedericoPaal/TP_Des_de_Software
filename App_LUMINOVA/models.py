from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.TextField(max_length=500)
    categoria = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=60)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_entrega = models.IntegerField() # Tiempo de entrega en días
    #imagen = models.ImageField(null=True, blank=True)
    proveedor = models.CharField(max_length=60)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.descripcion}"