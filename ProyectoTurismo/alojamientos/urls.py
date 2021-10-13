from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('',views.alojamientos, name='Alojamientos'),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    path('alojamiento_detalle/<int:alojamiento_id>/', views.alojamiento_detalle, name="categoria")
    

]
