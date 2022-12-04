from django.urls import re_path
from operaciones.views import OperacionesView

urlpatterns = [
    re_path(r'^ejercicio/', OperacionesView.as_view()),
    # re_path(r'^union/', UnionView.as_view()),
    # re_path(r'^interseccion/', InterseccionView.as_view()),
]
