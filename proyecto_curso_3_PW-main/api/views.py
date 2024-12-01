from .models import Libro
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import LibroSerializer

# Create your views here.
class LibroViewSet(viewsets.ModelViewSet):    
    """
    API-REST endpoint para el modelo carro, admite GET,
    POST, PUT, PATCH, DELETE
    """
    queryset = Libro.objects.all().order_by('-fecha_publicacion')  # Esto indica que queremos obtener todos los libros
    serializer_class = LibroSerializer  # Usamos el serializador que creamos anteriormente
