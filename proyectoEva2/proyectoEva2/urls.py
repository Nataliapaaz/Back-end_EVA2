"""
URL configuration for proyectoEva2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from formularioRamos import views as ramos_views
from formularioProfesor import views as profesor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formularioramos/', ramos_views.formulario_ramos, name='formularioramos'),
    path('', ramos_views.home, name='home'),
    # Path de ramos
    path('ramos/', ramos_views.ramosData, name='ramosData'),
    path('eliminar_ramo/<int:idRamo>/', ramos_views.eliminar_ramo, name='eliminar_ramo'),
    path('modificar_ramo/<int:idRamo>/', ramos_views.modificar_ramos, name='modificar_ramo'),
    # Path de profesores
    path('formularioprofesor/', profesor_views.formulario_profesor, name='formulario_profesor'),
    path('profesor/', profesor_views.profesorData, name='profesorData'),
    path('eliminar_profesor/<int:idProfesor>/', profesor_views.eliminar_profesor, name='eliminar_profesor'),
    path('modificar_profesor/<int:idProfesor>/', profesor_views.modificar_profesor, name='modificar_profesor'),
]