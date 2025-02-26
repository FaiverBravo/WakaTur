"""ProyectoTurismo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from RupestreApp import views


urlpatterns = [
    path('admin/', admin.site.urls),

    #enlace de urls entre Proyecto principal con App RupestreApp
    path('', include('RupestreApp.urls')),
    
    path('alojamientos/', include('alojamientos.urls')),
    path('experiencias/', include('experiencias.urls')),
    path('gastronomia/', include('gastronomia.urls')),
    path('servicios/', include('servicios.urls')),
    path('tienda/', include('tienda.urls')),
    path('contacto/', include('contacto.urls')),
    
    path('PupestreApp/', include('django.contrib.auth.urls')), 
    path('PupestreApp/', include('RupestreApp.urls')), 
    
   
]
