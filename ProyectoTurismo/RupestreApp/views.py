from django.shortcuts import render, HttpResponse

from .forms import loginUsuario


# Create your views here.

def index(request):

# login de ususario
    data={
            'form': loginUsuario()
        }
    if request.method =='POST':
        formulario = loginUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Usuario registrado satisfactoriamente!"
        else:
            data["form"] = formulario

    return render(request, "RupestreApp/index.html", data)

def nosotros(request):

    return render(request, "RupestreApp/nosotros.html")

def mapa(request):

    return render(request, "RupestreApp/mapa.html")


# API Formulario para contacto






    
