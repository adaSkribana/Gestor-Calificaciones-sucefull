from django.urls import path
from asignaturas import views

urlpatterns = [
    path('asignaturas/', views.lista_asignaturas, name='lista_asignaturas'),  # URL para gestionar asignaturas
    path('asignaturas/<int:pk>/', views.detalle_asignatura, name='detalle_asignatura'),  # Detalle de una asignatura específica
    path('asignaturas/nueva/', views.nueva_asignatura, name='nueva_asignatura'),  # URL para agregar una nueva asignatura
    path('asignaturas/<int:pk>/editar/', views.editar_asignatura, name='editar_asignatura'),  # URL para editar una asignatura existente
    
]
