# paginas/urls.py
from django.urls import path

from .views import vista_inicio, vista_acerca_de, vista_proyectos

urlpatterns = [
    path("", vista_inicio),
    path("acerca-de/", vista_acerca_de),  # nuevo
    path("proyectos/", vista_proyectos),

]
