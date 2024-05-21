from django.urls import path
from notas import views

urlpatterns = [
    path('notas/', views.lista_notas, name='lista_notas'),  # URL para gestionar notas
    path('notas/nueva/', views.nueva_nota, name='nueva_nota'),  # URL para agregar una nueva nota
    path('notas/<int:pk>/editar/', views.editar_nota, name='editar_nota'),  # URL para editar una nota existente
]
