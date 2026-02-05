from django.shortcuts import render


def index(request):
    datos = {
        "titulo": "Django",
        "descripcion": "Framework para crear aplicaciones web",
    }
    return render(request, "prueba/index.html", datos)


def notas(request):
    mis_notas = [10, 7, 6, 3, 8, 4]
    return render(request, "prueba/notas.html", {"notas": mis_notas})
