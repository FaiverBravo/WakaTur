from django.db import models

# Create your models here.

class Experiencia(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=250)
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to='experiencias')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='experiencia'
        verbose_name_plural='experiencias'

    def __str__(self):
        return self.nombre  