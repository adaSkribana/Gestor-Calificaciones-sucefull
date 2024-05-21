from django.urls import path
from autenticacion import views

app_name = 'autenticacion'  # Define el espacio de nombres para la aplicación

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # URL para registrarse
    path('login/', views.user_login, name='login'),  # URL para iniciar sesión
    path('logout/', views.user_logout, name='logout'),  # URL para cerrar sesión
    path('profile/', views.profile, name='profile'),  # URL para ver y editar el perfil del usuario
]
