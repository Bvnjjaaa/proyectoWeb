"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aplicacion import views as aplicacion_views
from usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', aplicacion_views.index, name='index'),
    path('servicios/', aplicacion_views.servicios, name='servicios'),
    path('clasesguitarra/', aplicacion_views.clasesguitarra, name='clasesguitarra'),
    path('calibracion/', aplicacion_views.calibracion, name='calibracion'),
    path('salaensayo/', aplicacion_views.salaensayo, name='salaensayo'),
    path('galeria/', aplicacion_views.galeria, name='galeria'),
    path('nosotros/', aplicacion_views.nosotros, name='nosotros'),
    path('blog/', aplicacion_views.blog, name='blog'),
    path('usuarios/', include('usuarios.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contacto/<int:id>/eliminar/', usuarios_views.contacto_eliminar, name='contacto_eliminar'),
    path('listacontactos/', usuarios_views.contacto_list, name='contacto_lista'),
    path('agregarcontacto/', usuarios_views.contacto_nuevo, name='contacto_nuevo'),
    path('contacto/<int:id>/editar/', usuarios_views.contacto_editar, name='contacto_editar'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]







