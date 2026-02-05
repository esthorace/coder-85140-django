from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais_origen = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, blank=True
    )
