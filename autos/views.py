from django.shortcuts import render
from .models import *

def principal(request):
    datos = {
        'titulo':'Principal'
    }
    return render(request,'principal.html',datos)

def autos(request):
    datos = {
        'titulo':'Autos',
        'autos':Autos.objects.all()
    }
    return render(request,'autos.html',datos)

def clientes(request):
    datos = {
        'titulo':'Clientes',
        'clientes':Clientes.objects.all()
    }
    return render(request,'clientes.html',datos)

