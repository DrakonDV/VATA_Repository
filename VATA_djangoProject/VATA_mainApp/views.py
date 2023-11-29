from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .models import testModel
from .models import Object, Place
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Si el inicio de sesión es exitoso, redirige a la página deseada
            return redirect('homeuser.html')
        else:
            # Mensaje de alerta si las credenciales son incorrectas
            messages.error(request, 'Revise sus datos e intente nuevamente', extra_tags='alert-danger')
            # Puedes redirigir de vuelta a la página de inicio de sesión o renderizarla nuevamente
            return render(request, 'formulariologuin.html')

    return render(request, 'formulariologuin.html')




def registro_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Verificar si las contraseñas coinciden
        if password != confirm_password:
            return render(request, 'formularioregistro.html', {'error': 'Las contraseñas no coinciden'})
        
        # Verificar si el usuario ya existe
        if User.objects.filter(email=email).exists():
            return render(request, 'formularioregistro.html', {'error': 'El usuario ya existe'})
        
        # Crear un nuevo usuario
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()
        
    
    return render(request, 'formularioregistro.html')





from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Favorito
@login_required
def agregar_eliminar_favorito(request, lugar_id):
    lugar = Place.objects.get(id=lugar_id)
    usuario = request.user
    
    # Verificar si el lugar ya es un favorito del usuario
    try:
        favorito_existente = Favorito.objects.get(usuario=usuario, lugar=lugar)
        # Si ya es un favorito, eliminarlo
        favorito_existente.delete()
        return JsonResponse({'favorito': False})
    except Favorito.DoesNotExist:
        # Si no es un favorito, agregarlo
        Favorito.objects.create(usuario=usuario, lugar=lugar)
        return JsonResponse({'favorito': True})


def homeuser(request):
    return render(request, 'homeuser.html')

def ayuda(request):
    return render(request, 'paginadeayuda.html')

def mostrar_formulario(request):
    return render(request, 'formulario.html')

def guardar_lugar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        location = request.POST.get('location')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')
        categoria = request.POST.get('categoria')

        nuevo_lugar = Place(placeName=nombre, location=location, descripcion=descripcion, placeImage=imagen, placeCategory=categoria)
        nuevo_lugar.save()
        print(nombre, location,descripcion, imagen, categoria)

        return redirect( 'index')  # Puedes renderizar una página de confirmación o redirigir a otra vista
    else:
        return redirect( 'mostrar_formulario')  # Si la solicitud no es POST, muestra el formulario nuevamente
    

def index(request):
    template = loader.get_template("mainGUI/index.html")
    return render(request, "mainGUI/index.html", {})

def S2ndView(request, lugar):
    dataLugares = Place.objects.all()
    dataObjetos = Object.objects.all()
    print("lugares", dataLugares)
    return render(request, "mainGUI/2ndView.html", {'dataLugares': dataLugares, "dataObjetos": dataObjetos, "receivedData": lugar})

def ShowData(request):
    dataLugares = Place.objects.all()
    dataObjetos = Object.objects.all()
    print("lugares", dataLugares)
    return render(request, "mainGUI/test.html", {'dataLugares': dataLugares, "dataObjetos": dataObjetos})

def mostrar_lugar(request, Place_id):
    Place_id=1
    lugar=Place.objects.get(pk=Place_id)
    return render(request,"2ndView.html",{"Place": lugar})

from django.shortcuts import render
from .models import Favorito

def favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user)
    return render(request, 'user.html', {'favoritos': favoritos})

    



