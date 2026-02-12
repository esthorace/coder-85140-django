from django.shortcuts import redirect, render

from . import models
from .forms import PaisForm


def index(request):
    datos = {
        "titulo": "Django",
        "descripcion": "Framework para crear aplicaciones web",
    }
    return render(request, "prueba/index.html", datos)


def notas(request):
    mis_notas = [10, 7, 6, 3, 8, 4]
    return render(request, "prueba/notas.html", {"notas": mis_notas})


def tirar_dado(request):
    from datetime import datetime
    from random import randint

    tiro_de_dado = randint(1, 6)

    if tiro_de_dado == 6:
        mensaje = f"Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😊 ✨ Ganaste ✨"
    else:
        mensaje = f"Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😒 Sigue intentando. Presiona F5"

    datos = {
        "title": "Tiro de Dados",
        "mensaje": mensaje,
        "fecha": datetime.now().strftime("%H:%M:%S.%f"),
    }
    return render(request, "prueba/dados.html", context=datos)


def clientes_listar(request):
    clientes = models.Cliente.objects.all()
    return render(request, "prueba/clientes.html", context={"clientes": clientes})


def paises_listar(request):
    paises = models.Pais.objects.all()
    return render(request, "prueba/paises.html", context={"paises": paises})


def paises_crear(request):
    if request.method == "POST":
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("paises_listar")
    else:
        form = PaisForm()
    return render(request, "prueba/paises_crear.html", {"form": form})
