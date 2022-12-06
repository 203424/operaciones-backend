from django.urls import re_path
from operaciones.views import OperacionesView,EjercicioView

urlpatterns = [
    re_path(r'^ejercicio/(?P<op>\w+)/', OperacionesView.as_view()),
    re_path(r'^quiz/opciones/', EjercicioView.as_view()),
    re_path(r'^quiz/(?P<op>\w+)/', EjercicioView.as_view()),
    re_path(r'^(?P<operacion>\w+)/', OperacionesView.as_view()),
]
