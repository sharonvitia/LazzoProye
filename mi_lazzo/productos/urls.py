from django.urls import path
from . import views

urlpatterns = [
    # Vistas públicas
    path('', views.productos_publicos, name='productos_publicos'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),
    path('detalle/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    
    # Vistas para emprendedores
    path('publicar/', views.publicar_producto, name='publicar_producto'),
    path('mis-productos/', views.mis_productos, name='mis_productos'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]