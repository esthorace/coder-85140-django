from django.shortcuts import render


def index(request):
    return render(request, "prueba/index.html", {"titulo": "Python🔥"})
