from .models import Libro  # Importamos el modelo Libro
from rest_framework import viewsets  # Importamos la librería para crear ViewSets
from rest_framework.response import Response  # Importamos la librería para crear ViewSets
from .serial import LibroSerializer  # Importamos el serializador para el modelo Libro

#Conjunto de visitas para el CRUD del modelo libros
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('-fecha_publicacion')  # Esto indica que queremos obtener todos los libros
    serializer_class = LibroSerializer  # Usamos el serializador que creamos anteriormente