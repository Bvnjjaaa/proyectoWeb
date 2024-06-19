from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

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

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        numero = request.POST.get('numero')
        correo = request.POST.get('correo')

        return HttpResponseRedirect(reverse('index'))
    return render(request, 'index.html')
