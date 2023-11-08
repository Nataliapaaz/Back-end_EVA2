from django.shortcuts import render
from django.http import HttpResponse
from formularioRamos.models import Ramos
from django.shortcuts import render
from .forms import RamosForm 

# Create your views here.
def renderTemplate(request):
    return render(request, "formularioRamos/formularioRamos.html")

def ramosData (request):
    ramos = Ramos.objects.all ()
    data = {'ramos' : ramos}
    return render (request, 'ramos/ramos.html', data)

def formulario_ramos(request):
    if request.method == 'POST':
        form = RamosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RamosForm()
    return render(request, 'formularioRamos.html', {'form': form})