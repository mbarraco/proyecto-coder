from django.http import HttpResponse

from django.template import loader
from django.shortcuts import render

# Create your views here.

from AppCoder.models import Profesor


def crear_profesor(request):
    template = loader.get_template("template1.html")

    profe = Profesor(nombre="Ricardo", apellido="Ruben", email="ricky@coder.com", profesion="abogado")
    profe_2 = Profesor(nombre="Manuel", apellido="Saenz", email="manu@coder.com", profesion="abogado")
    profe_3 = Profesor(nombre="Ezequiel", apellido="Bartella", email="eze@coder.com", profesion="contador")
    
    dict_de_contexto = {
        "profe_1": profe,
        "profe_2": profe_2,
        "profe_3": profe_3,
    }

    res = template.render(dict_de_contexto)

    return HttpResponse(res)