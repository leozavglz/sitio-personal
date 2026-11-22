# paginas/urls.py
from django.urls import path

from .views import (
    vista_inicio,
    VistaProyectos,
    VistaAcercaDe,
    vista_saludo,
    vista_cuadrado,
)

urlpatterns = [
    path("", vista_inicio, name="inicio"),  # nuevo
    path("acerca-de/", VistaAcercaDe.as_view(), name="acerca_de"),  # nuevo
    path("proyectos/", VistaProyectos.as_view(), name="proyectos"),
    path("saludo/<str:nombre>/", vista_saludo, name="saludo"),  # nuevo
    path("cuadrado/<int:numero>/", vista_cuadrado, name="cuadrado"),  # nuevo
]
