from django.db import models

# Create your models here.

class Gastronomia(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to='gastronomia')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='gastronomia'
        verbose_name_plural='gastronomias'

    def __str__(self):
        return self.nombre  