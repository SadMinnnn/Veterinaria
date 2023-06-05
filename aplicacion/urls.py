"""
URL configuration for aplicacion project.

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
from django.urls import path,include
from veterinaria.views import HistoriaClinica
from veterinaria.views import Registrar
from veterinaria.views import IniciarSesion
from veterinaria.views import VentasMedicamentos
from veterinaria.views import RecetarMedicamentos
from veterinaria.views import ConsultarVentasMedicamentos
from veterinaria.views import ConsultarRecetarMedicamentos
from veterinaria.views import RegistrarMascota
from veterinaria.views import MedicoVeterinario
from veterinaria.views import ConsultarMascotasRegistradas
from veterinaria.views import ConsultarHistoriaClinica
from veterinaria.views import ActualizarRegistrarMascota
from veterinaria.views import ActualizarHistoriaClinica
from veterinaria.views import ActualizarVentasMedicamentos
from veterinaria.views import ActualizarRecetarMedicamentos
from veterinaria.views import EliminarRegistrarMascota
from veterinaria.views import EliminarRegistrarMascota
from veterinaria.views import EliminarHistoriaClinica
from veterinaria.views import EliminarVentasMedicamentos
from veterinaria.views import EliminarRecetarMedicamentos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IniciarSesion, name='IniciarSesion'),
    path('Registrar/', Registrar,name='Registrar'),
    path('VentasMedicamentos/', VentasMedicamentos, name='VentasMedicamentos'),
    path('RecetarMedicamentos/', RecetarMedicamentos,name='RecetarMedicamentos'),
    path('ConsultarVentasMedicamentos/', ConsultarVentasMedicamentos, name='ConsultarVentasMedicamentos'),
    path('ConsultarRecetarMedicamentos/', ConsultarRecetarMedicamentos,name='ConsultarRecetarMedicamentos'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('RegistrarMascota/', RegistrarMascota,name='RegistrarMascota'),
    path('HistoriaClinica/', HistoriaClinica,name='HistoriaClinica'),
    path('MedicoVeterinario/', MedicoVeterinario,name='MedicoVeterinario'),
    path('ConsultarMascotasRegistradas/', ConsultarMascotasRegistradas,name='ConsultarMascotasRegistradas'),
    path('ConsultarHistoriaClinica/', ConsultarHistoriaClinica,name='ConsultarHistoriaClinica'),
    path('ActualizarVentasMedicamentos', ActualizarVentasMedicamentos, name='ActualizarVentasMedicamentos'),
    path('ActualizarRegistrarMascota', ActualizarRegistrarMascota, name='ActualizarRegistrarMascota'),
    path('ActualizarHistoriaClinica', ActualizarHistoriaClinica, name='ActualizarHistoriaClinica'),
    path('ActualizarRecetarMedicamentos', ActualizarRecetarMedicamentos, name='ActualizarRecetarMedicamentos'),
    path('EliminarRegistrarMascota', EliminarRegistrarMascota, name='EliminarRegistrarMascota'),
    path('EliminarHistoriaClinica', EliminarHistoriaClinica, name='EliminarHistoriaClinica'),
    path('EliminarVentasMedicamentos', EliminarVentasMedicamentos, name='EliminarVentasMedicamentos'),
    path('EliminarRecetarMedicamentos', EliminarRecetarMedicamentos, name='EliminarRecetarMedicamentos'),

]

