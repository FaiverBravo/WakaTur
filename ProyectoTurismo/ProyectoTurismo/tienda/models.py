from django.db import models

# Create your models here.
class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="CategoriaProd"
        verbose_name_plural="CategoriasProd"
        
    def __str__(self):
        return self.nombre


# tipo_alojamiento =[
#     [0, "Hoteles"],
#     [1, "Cabaña"],
#     [2, "Hostal y pensiones"],
#     [3, "Camping"],
#     [4, "Glamping"],
#     [5, "Apartamentos"],
#     [6, "Alberges"],
# ]
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    # tipo_alojamiento=models.IntegerField(choices=tipo_alojamiento)
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
        
        # def __str__(self):
        
        #         return self.nombre