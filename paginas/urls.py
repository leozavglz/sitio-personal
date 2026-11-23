# paginas/urls.py
from django.urls import path

from .views import (
    VistaAcercaDe,
    VistaInicio,
    VistaProyectos,
    vista_cuadrado,
    vista_saludo,
)

urlpatterns = [
    path("", VistaInicio.as_view(), name="inicio"),
    path("acerca-de/", VistaAcercaDe.as_view(), name="acerca_de"),
    path("proyectos/", VistaProyectos.as_view(), name="proyectos"),
    path("saludo/<str:nombre>/", vista_saludo, name="saludo"),
    path("cuadrado/<int:numero>/", vista_cuadrado, name="cuadrado"),
]
