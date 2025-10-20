from django.urls import path
from . import views

urlpatterns = [
    # Páginas iniciales
    path('inicio/', views.inicio, name='inicio'),
    path('seleccion-tipo/', views.seleccion_tipo_usuario, name='seleccion_tipo'),
    
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('invitado/', views.invitado_view, name='invitado'),
    
    # Registro
    path('registro/emprendedor/', views.registro_emprendedor, name='registro_emprendedor'),
    path('registro/consumidor/', views.registro_consumidor, name='registro_consumidor'),
    
    # Dashboards
    path('home/', views.home_view, name='home'),
    path('home/emprendedor/', views.home_emprendedor, name='home_emprendedor'),
    path('home/consumidor/', views.home_consumidor, name='home_consumidor'),
]



