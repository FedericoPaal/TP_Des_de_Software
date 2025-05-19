from django import forms
from .models import Insumo

class ProductoFormulario(forms.ModelForm):
    creacion = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    class Meta:
        model = Insumo
        fields = '__all__'