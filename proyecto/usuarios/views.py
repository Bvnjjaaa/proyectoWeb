from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from aplicacion.forms import ContactoForm
from aplicacion.models import Contacto


@login_required
def contacto_list(request):
    contactos = Contacto.objects.all()
    return render(request, 'usuarios/contacto_lista.html', {'contactos': contactos})

def contacto_nuevo(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            if 'from_crud' in request.POST:
                return redirect('contacto_lista')  # Redirigir a la lista de contactos
            else:
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

@login_required
def contacto_editar(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contacto_lista')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'usuarios/contacto_editar.html', {'form': form})