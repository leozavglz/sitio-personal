# paginas/views.py
from django.shortcuts import render


def vista_inicio(request):
    contexto = {
        "habilidades": ["Python", "Django", "Git"],
        "mensaje": "GRACIAS por VISITAR mi sitio.",
    }
    return render(request, "inicio.html", contexto)


def vista_acerca_de(request):  # nuevo
    contexto = {
        "nombre": "Leonardo",
        "edad": 25,
    }
    return render(request, "acerca_de.html", contexto)


def vista_proyectos(request):
    contexto = {
        "proyectos": [
            "SaaS de automatizaciones en Python",
            "Algun juego que utilice WebGPU",
            "Sitio para mis finanzas a la medida",
        ],
    }
    return render(request, "proyectos.html", contexto)
