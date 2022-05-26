from django.urls import path, include


from RupestreApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',views.index, name='Inicio'),
    path('nosotros/',views.nosotros, name='Nosotros'),
    path('mapa/',views.mapa, name='Mapa'),
    path('registro/',views.registro, name='Registro'),
    
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)