# paginas/views.py
from django.shortcuts import render
from django.views.generic import TemplateView  # nuevo


def vista_inicio(request):
    contexto = {
        "habilidades": ["Python", "Django", "Git"],
        "mensaje": "GRACIAS por VISITAR mi sitio.",
    }
    return render(request, "inicio.html", contexto)


class VistaAcercaDe(TemplateView):  # nuevo
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