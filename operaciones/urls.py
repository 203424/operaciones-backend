from django.urls import re_path
from operaciones.views import OperacionesView, UnionView

urlpatterns = [
    re_path(r'^ejercicio/(?P<op>\w+)/', OperacionesView.as_view()),
    re_path(r'^union/', UnionView.as_view()),
    # re_path(r'^interseccion/', InterseccionView.as_view()),
]
