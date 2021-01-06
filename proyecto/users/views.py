from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from users.forms import RegistroForm
from .models import Imagen
from .forms import ImagenForm

def pagina(request):
    return render(request, "users/pagina.html")


def inicio(request):
    if request.user.is_authenticated:
        return render(request, "users/inicio.html")
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
    imagenes = Imagen.objects.all()
    contexto = {'imagenes': imagenes}
    return render(request, 'imagenes/index.html', contexto)

def loadPicture(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = ImagenForm()
    contexto = {'form': form}
    return render(request, 'imagenes/load.html', contexto)
