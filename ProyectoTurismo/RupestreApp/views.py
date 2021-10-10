from django.shortcuts import render, HttpResponse



# Create your views here.

def index(request):

    return render(request, "RupestreApp/index.html")

def nosotros(request):

    return render(request, "RupestreApp/nosotros.html")

def mapa(request):

    return render(request, "RupestreApp/mapa.html")


    
