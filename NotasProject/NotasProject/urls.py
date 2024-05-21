from django.contrib import admin
from django.urls import path, include
from NotasProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Página de inicio
    path('notas/', include('notas.urls')),  # Prefijo 'notas'
    path('alumnos/', include('alumnos.urls')),  # Prefijo 'alumnos'
    path('asignaturas/', include('asignaturas.urls')),  # Prefijo 'asignaturas'
    path('autenticacion/', include('autenticacion.urls')),  # Prefijo 'autenticacion'
]
