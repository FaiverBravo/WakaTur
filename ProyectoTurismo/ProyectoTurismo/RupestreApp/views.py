from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def index(request):

    return render(request, "RupestreApp/index.html")

def nosotros(request):

    return render(request, "RupestreApp/nosotros.html")

def mapa(request):

    return render(request, "RupestreApp/mapa.html")

def registro(request):
    # if request.method == 'POST':
    #     form =UserCreationForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']        
    #         messages.succes(request,f'Usuario {username} creado')
    #         return redirect('home')
    # else:
    #     form= UserCreationForm()
        
    # context = {'form': form}
    return render(request, "RupestreApp/authentication/registro.html" )


def login_user(request):
# login de ususario
    
    if request.method =='POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            ...
        else:
            messages.success(request, ("There Was Error Logging In, Try Again..."))
            return redirect('login')
            ...

    else:
        return render(request, "RupestreApp/authentication/login.html")

def home(request):

    return render(request, "RupestreApp/home.html")

    
