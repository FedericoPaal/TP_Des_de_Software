"""
URL configuration for Proyecto_LUMINOVA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'App_LUMINOVA'

urlpatterns = [
    path("", inicio, name="inicio"),
    path("compras/", compras, name="compras"),
    path("produccion/", produccion, name="produccion"),
    path("ventas/", ventas, name="ventas"),
    path("deposito/", deposito, name="deposito"),
    path("control_calidad/", control_calidad, name="control_calidad"),

    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='App_LUMINOVA:inicio'), name='login'),  # Página de login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Cerrar sesión

#  Paths para los botones del sidebar de Admin

    path('dashboard/', dashboard_view, name='dashboard'),
    path('usuarios/', usuarios, name='usuarios'),
    path('roles-permisos/', roles_permisos, name='roles-permisos'),
    path('auditoria/', auditoria, name='auditoria'),

#  Paths para los botones del sidebar de Produccion
    path('ordenes/', ordenes, name='ordenes'),
    path('planificacion/', planificacion, name='planificacion'),
    path('reportes/', reportes, name='reportes'),
]