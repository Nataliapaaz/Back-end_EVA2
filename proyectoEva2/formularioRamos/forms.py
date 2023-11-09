from django import forms
from .models import Ramos

class RamosForm(forms.ModelForm):

        model = Ramos
        fields = '__all__'