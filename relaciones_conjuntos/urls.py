from django.urls import path, re_path
from django.conf.urls import include

# Importacion de vistas
from relaciones_conjuntos.views import RelacionesConjuntos, EjercicioRelacion

urlpatterns = [
   re_path(r'^validar/$', RelacionesConjuntos.as_view()),
   re_path(r'^ejercicio/$', EjercicioRelacion.as_view()),
]