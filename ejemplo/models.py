from django.db import models

# Create your models here.
class Producto(models.Model):
    
    nombre = models.CharField(max_length=50, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} | Precio: {self.precio}'
    
    def serialize(self):
        return {
            'nombre' : self.nombre,
            'precio' : self.precio
        }