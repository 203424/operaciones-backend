from django.urls import re_path
from operaciones.views import OperacionesView

urlpatterns = [
    re_path(r'^ejercicio/(?P<op>\w+)/', OperacionesView.as_view()),
    re_path(r'^(?P<operacion>\w+)/', OperacionesView.as_view()),
]
