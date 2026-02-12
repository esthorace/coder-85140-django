from tabnanny import verbose

from django.db import models


class Pais(models.Model):
    nombre = models.CharField(
        max_length=100, unique=True, verbose_name="Nombre del país"
    )

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name_plural = "Países"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais_origen = models.ForeignKey(
        Pais,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="País de origen",
    )

    def __str__(self) -> str:
        return f"{self.apellido.upper()}, {self.nombre}"

    class Meta:
        verbose_name_plural = "Clientes"
