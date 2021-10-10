from django.shortcuts import render

#from tiendas.models import Tienda

# Create your views here.

def tienda(request):
    #tiendas=Tienda.objects.all()
    return render(request, "tienda/tienda.html")

