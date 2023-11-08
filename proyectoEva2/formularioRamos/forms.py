from django import forms
from .models import Ramos

class RamosForm(forms.ModelForm):
    class Meta:
        model = Ramos
        fields = '__all__'