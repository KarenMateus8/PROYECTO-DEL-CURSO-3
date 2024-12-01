from django.db import models

#Modelo que representa la estructura de datos de un registro 
#correspondiente a un libro en base de datos

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()  
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo
    
