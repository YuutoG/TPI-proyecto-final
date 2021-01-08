from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from users.forms import RegistroForm
from .models import Imagen, Favorito, Tarde
from .forms import ImagenForm




def pagina(request):
    return render(request, "users/pagina.html")


def inicio(request):
    if request.user.is_authenticated:
        imagenes = Imagen.objects.all().order_by('fecha_subida')[:100][::-1]
        contexto = {'imagenes': imagenes}
        return render(request, "users/inicio.html", contexto)
    return redirect('/login')

def signup(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistroForm()

    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None    
    return render(request, 'registration/signup.html', {
        'form': form
        })


def login(request):
    # formulario de autenticacion
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # recuperar las credenciales v
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Verificar credenciales del usuario
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/inicio')
    return render(request, "users/login.html", {'form': form})


def logout(request):
    do_logout(request)
    return redirect('/inicio')


def profile(request):
    imagenes = Imagen.objects.all().filter(user=request.user)
    contexto = {'imagenes': imagenes}
    return render(request, 'imagenes/perfil.html', contexto)

def loadPicture(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            foto = form.save(commit=False)
            foto.user= request.user
            foto.save()
            return redirect('profile')
    form = ImagenForm()
    contexto = {'form': form}
    return render(request, 'imagenes/load.html', contexto)

def viewFavorito(request):
    if request.method == 'POST':
        idimagen=int(request.POST['idImagen'])
        imagen=Imagen.objects.get(pk=idimagen)
        user=request.user
        fav=Favorito(idImagen=imagen,user=user)
        if fav.clean() != 1:
            fav.save()
            return redirect('favorito')
        else:
            return redirect('favorito')
def viewEliminarImagen(request):
    if request.method == 'POST':
        idimagen=int(request.POST['idImagen'])
        instancia= Imagen.objects.get(id=idimagen)
        instancia.delete()
        return redirect('/profile')

def viewEliminarFavorito(request):
    if request.method == 'POST':
        idimagen=int(request.POST['idImagen'])
        instancia= Favorito.objects.get(id=idimagen)
        instancia.delete()
        return redirect('favorito')
def viewFavoritos(request):
    imagenes = Favorito.objects.all().filter(user=request.user)
    contexto = {'imagenes': imagenes}
    return render(request, 'imagenes/favorito.html', contexto)

def viewTarde(request):
    if request.method == 'POST':
        idimagen=int(request.POST['idImagen'])
        imagen=Imagen.objects.get(pk=idimagen)
        user=request.user
        fav=Tarde(idImagen=imagen,user=user)
        if fav.clean() != 1:
            fav.save()
            return redirect('viewVerMasTarde')
        else:
            return redirect('viewVerMasTarde')

def viewVerMasTarde(request):
    imagenes = Tarde.objects.all().filter(user=request.user)
    contexto = {'imagenes': imagenes}
    return render(request, 'imagenes/tarde.html', contexto)

def viewEliminarTarde(request):
    if request.method == 'POST':
        idimagen=int(request.POST['idImagen'])
        instancia= Tarde.objects.get(id=idimagen)
        instancia.delete()
        return redirect('viewVerMasTarde')

def viewBusqueda(request):
    imagenes = Imagen.objects.all().filter(titulo__contains=request.GET['idImagen'])
    contexto = {'imagenes': imagenes}
    return render(request, 'imagenes/busqueda.html', contexto)



