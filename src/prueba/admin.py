from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Cliente)
admin.site.register(models.Pais)
