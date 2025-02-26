from django.shortcuts import render

from experiencias.models import Experiencia

# Create your views here.

def experiencias(request):
    experiencias=Experiencia.objects.all()
    return render(request, "experiencias/experiencias.html", {"experiencias": experiencias})


