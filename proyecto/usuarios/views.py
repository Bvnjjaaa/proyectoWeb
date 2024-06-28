from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from aplicacion.forms import ContactoForm
from aplicacion.models import Contacto
from aplicacion.views import index

@login_required
def contacto_list(request):
    contactos = Contacto.objects.all()
    return render(request, 'usuarios/contacto_lista.html', {'contactos': contactos})

@login_required
def contacto_nuevo(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactoForm()
    return render(request, 'usuarios/contacto_agregar.html', {'form': form})

@login_required
def contacto_eliminar(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == "POST":
        contacto.delete()
        return redirect('contacto_lista')
    return render(request, 'usuarios/contacto_confirmar_eliminar.html', {'contacto': contacto})
