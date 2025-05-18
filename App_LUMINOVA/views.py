from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages

# Create your views here.

#  Funciones para las vistas del navbar
def compras(req):
    return render(req, "compras.html")

def produccion(req):
    return render(req, "produccion.html")

def ventas(req):
    return render(req, "ventas.html")

def deposito(req):
    return render(req, "deposito.html")

def control_calidad(req):
    return render(req, "control_calidad.html")

def inicio(request):
    if request.user.is_authenticated:
        return redirect('App_LUMINOVA:dashboard')  # Redirige al dashboard si está autenticado
    return redirect('App_LUMINOVA:login')  # Redirige al login si no está autenticado

#  Funciones para el login y logout
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard.html')

    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if user:
            login(request, user)
            return redirect('App_Luminova:dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login.html')

#  Funciones para los botones del sidebar del Admin
def usuarios(request):
    return render(request, 'usuarios.html')

def roles_permisos(request):
    return render(request, 'roles_permisos.html')

def auditoria(request):
    return render(request, 'auditoria.html')

#  Funciones para los botones del sidebar de Compras
def desglose(req):
    return render(req, "desglose.html")

def seguimiento(req):
    return render(req, "seguimiento.html")

def tracking(req):
    return render(req, "tracking.html")

def desglose2(req):
    return render(req, "desglose2.html")

#  Funciones para los botones del sidebar de Produccion
def ordenes(request):
    return render(request, 'ordenes.html')

def planificacion(request):
    return render(request, 'planificacion.html')

def reportes(request):
    return render(request, 'reportes.html')

#  Funciones para el boton Seleccionar de la tabla de OP// los botones del sidebar de Deposito
def depo_seleccion(request):
    return render(request, 'depo_seleccion.html')

def depo_enviar(request):
    return render(request, 'depo_enviar.html')


