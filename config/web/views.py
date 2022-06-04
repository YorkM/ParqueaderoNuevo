from django.shortcuts import render

from web.models import Tarifas

# Create your views here.

def Home(request):
    # Usando el modelo para importar datos de bd
    tarifas = Tarifas.objects.all()

    # Crear un diccionario con los datos a enviar
    diccionario = {
        'tarifas': tarifas
    }

    return  render(request, 'index.html', diccionario)

def Tarifa(request):
    return  render(request, 'Tarifa.html')


