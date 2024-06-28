from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm

def contacto_list(request):
    contactos = Contacto.objects.all()
    return render(request, 'web/contacto_lista.html', {'contactos': contactos})

def contacto_nuevo(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_lista')
    else:
        form = ContactoForm()
    
    return render(request, 'web/contacto_agregar.html', {'form': form})

def contacto_eliminar(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('contacto_lista')
    return render(request, 'web/contacto_confirmar_eliminar.html', {'contacto': contacto})

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

