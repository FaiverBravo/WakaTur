from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Modelo Categorias
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre  

# Modelo Alojamientos
class Alojamiento(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=150)
    imagen=models.ImageField(upload_to='alojamientos')
    precio=models.IntegerField( null=True, blank=True)#opcional subir precio
    categorias=models.ManyToManyField(Categoria) #relación de muchos a muchos entre Categoria y Post
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='alojamiento'
        verbose_name_plural='alojamientos'

    def __str__(self):
        return self.nombre  

# Modelo Post para manejar comentarios 
class Post(models.Model):
    autor=models.ForeignKey(User, on_delete=models.CASCADE)#relación de uno a muchos entre autor y Post
    descripcion=models.CharField(max_length=150)    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.descripcion  



