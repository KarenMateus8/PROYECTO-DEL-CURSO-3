from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()  
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
       return f"{self.titulo} {self.autor} - Precio: {self.precio}"

