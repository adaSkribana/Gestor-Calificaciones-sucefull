from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alumnos, name='lista_alumnos'),
    path('nuevo/', views.nuevo_alumno, name='nuevo_alumno'),
    path('<int:pk>/', views.detalle_alumno, name='detalle_alumno'),
    path('<int:pk>/editar/', views.editar_alumno, name='editar_alumno'),
]
