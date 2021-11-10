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

# opciones_alojamiento = [
#     [0, "Hoteles"],
#     [1, "Cabañas"],
#     [2, "Hostales"],
#     [3, "Camping"],
#     [4, "Glamping"],
#     [5, "Apartamentos y casas"]
# ]
class Alojamiento(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=150)
    imagen=models.ImageField(upload_to='alojamientos')
    precio=models.IntegerField( null=True, blank=True)#opcional subir precio
    #tipo_alojamiento=models.IntegerField(choices=opciones_alojamiento)
    categorias=models.ManyToManyField(Categoria) #relación de muchos a muchos entre Categoria y Post
    disponibilidad=models.BooleanField(default=True)
    activo=models.BooleanField(default=True)# prendido o apagado
    # Horario

    abrir=models.TimeField(null=True)
    cerrar=models.TimeField(null=True)
    
    created=models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
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



