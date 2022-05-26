from django.shortcuts import render, HttpResponse

from .forms import loginUsuario

from django.contrib.auth.models import User
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

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email='faiver@gmail.com'

        User.objects.create_user(username, email, password)
        
        return render(request, "RupestreApp/autenticacion/registro.html", {
            'username':username,
            'password':password
            })

    return render(request, "RupestreApp/autenticacion/registro.html", {
            })

def login(request):

    return render(request, "RupestreApp/autenticacion/login.html")

def home(request):

    return render(request, "RupestreApp/home.html")

    
