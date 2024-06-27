from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    numero = models.CharField(max_length=20)
    correo = models.EmailField()
    rut = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'