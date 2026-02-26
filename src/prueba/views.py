from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
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


# **************************************

# def paises_listar(request):
#     consulta = request.GET.get("consulta")
#     if consulta:
#         paises = models.Pais.objects.filter(nombre__contains=consulta)
#     else:
#         paises = models.Pais.objects.all()
#     return render(request, "prueba/paises.html", context={"paises": paises})

class PaisList(ListView):
    model = models.Pais
    # template_name = "prueba/paises.html"
    # context_object_name = "paises"

    def get_queryset(self):
        consulta = self.request.GET.get("consulta")
        if consulta:
            paises = models.Pais.objects.filter(nombre__contains=consulta)
        else:
            paises = models.Pais.objects.all()
        return paises

# def paises_crear(request):
#     if request.method == "POST":
#         form = PaisForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("paises_listar")
#     else:
#         form = PaisForm()
#     return render(request, "prueba/paises_crear.html", {"form": form})

class PaisCreate(CreateView):
    model = models.Pais
    form_class = PaisForm
    success_url = reverse_lazy("paises_listar")


# def paises_ver(request, pk: int):
#     pais = models.Pais.objects.get(id=pk)
#     return render(request, "prueba/paises_ver.html", {"pais": pais})


class PaisDetail(DetailView):
    model = models.Pais


# def paises_editar(request, pk: int):
#     pais = models.Pais.objects.get(id=pk)

#     if request.method == "POST":
#         form = PaisForm(request.POST, instance=pais)
#         if form.is_valid():
#             form.save()
#             return redirect("paises_listar")
#     else:
#         form = PaisForm(instance=pais)
#     return render(request, "prueba/paises_crear.html", {"form": form})


class PaisUpdate(UpdateView):
    model = models.Pais
    form_class = PaisForm
    success_url = reverse_lazy("paises_listar")


# def paises_borrar(request, pk: int):
#     pais = models.Pais.objects.get(id=pk)
#     if request.method == "POST":
#         pais.delete()
#         return redirect("paises_listar")
#     return render(request, "prueba/paises_borrar.html", {"pais": pais})

class PaisDelete(DeleteView):
    model = models.Pais
    success_url = reverse_lazy("paises_listar")