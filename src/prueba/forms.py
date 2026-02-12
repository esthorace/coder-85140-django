from django import forms

from .models import Pais


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = "__all__"
        # fields = ['nombre']

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener más de 2 caracteres")
        return nombre
