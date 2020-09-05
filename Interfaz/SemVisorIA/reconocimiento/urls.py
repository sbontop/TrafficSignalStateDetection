from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargar_imagen, name='cargar_imagen'),
    path('imagen/<id>/', views.mostrar_imagen, name='mostrar_imagen'),
]