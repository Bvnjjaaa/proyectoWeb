from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'web/index.html')

def servicios(request):
    return render(request, 'web/servicios.html')

def clasesguitarra(request):
    return render(request, 'web/clasesguitarra.html')

def calibracion(request):
    return render(request, 'web/calibracion.html')

def salaensayo(request):
    return render(request, 'web/salaensayo.html')

def galeria(request):
    return render(request, 'web/galeria.html')

def nosotros(request):
    return render(request, 'web/nosotros.html')

def blog(request):
    return render(request, 'web/blog.html')
