from django.db import models
from django.db.models.fields import CharField

# Create your models here.

opciones_usuario = [
    [0, "Alojamiento"],
    [1, "Experiencia"],
    [2, "Gastronomia"],
    [3, "Servicio"],
    [4, "Tienda"],
]
class loginUsuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    email = models.EmailField()
    tipo_usuario=models.IntegerField(choices=opciones_usuario)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    def __str__(self) :
        return self.nombre_usuario

