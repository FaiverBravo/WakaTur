from django.shortcuts import render

from gastronomia.models import Gastronomia

# Create your views here.

def gastronomia(request):
    gastronomia=Gastronomia.objects.all()
    return render(request, "gastronomia/gastronomia.html", {"gastronomia": gastronomia})