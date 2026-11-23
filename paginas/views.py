# paginas/views.py
from django.shortcuts import render
from django.views.generic import TemplateView


class VistaInicio(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["habilidades"] = ["Python", "Django", "Git"]
        contexto["mensaje"] = "GRACIAS por VISITAR mi sitio."
        return contexto


class VistaAcercaDe(TemplateView):
    template_name = "acerca_de.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nombre"] = "Leonardo"
        contexto["edad"] = 25
        return contexto


class VistaProyectos(TemplateView):
    template_name = "proyectos.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["proyectos"] = [
            "SaaS de automatizaciones en Python",
            "Algun juego que utilice WebGPU",
            "Sitio para mis finanzas a la medida",
        ]
        return contexto


def vista_saludo(request, nombre):
    return render(request, "saludo.html", {"nombre": nombre})


def vista_cuadrado(request, numero):
    contexto = {
        "numero": numero,
        "cuadrado": numero**2,
    }
    return render(request, "cuadrado.html", contexto)