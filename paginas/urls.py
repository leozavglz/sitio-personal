# paginas/urls.py
from django.urls import path

from .views import vista_inicio, VistaProyectos, VistaAcercaDe


urlpatterns = [
    path("", vista_inicio),
    path("acerca-de/", VistaAcercaDe.as_view()),  # nuevo
    path("proyectos/", VistaProyectos.as_view()),
]   


