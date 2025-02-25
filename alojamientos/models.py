from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Modelo Categorias
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

# Modelo Alojamientos
class Alojamiento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='alojamientos')
    precio = models.IntegerField(null=True, blank=True)
    categorias = models.ManyToManyField(Categoria)
    disponibilidad = models.BooleanField(default=True)
    habitaciones_disponibles = models.IntegerField(default=0)
    abrir = models.TimeField(null=True)
    cerrar = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now_add=True)
    # latitud = models.FloatField() 
    # longitud = models.FloatField()

    class Meta:
        verbose_name = 'alojamiento'
        verbose_name_plural = 'alojamientos'

    def __str__(self):
        return self.nombre

# Modelo Post para manejar comentarios
class Post(models.Model):
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE, related_name='posts')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.descripcion