from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/registro/', views.guardar_producto, name='guardar_producto'),
    path('productos/lista/', views.lista_productos, name='lista_productos'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
