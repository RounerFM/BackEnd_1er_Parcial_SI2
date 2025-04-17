from django.db import models

# Create your models here.
class Roles(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)


class TipoDePago(models.Model):
    nombre = models.CharField(max_length=100)


class Categorias(models.Model):
    nombre = models.CharField(max_length=100)


class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)



class Descuento(models.Model):
    nombre = models.CharField(max_length=50)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=100)
    fechaIni = models.DateTimeField(auto_now_add=True)
    fechaFin = models.DateTimeField(auto_now_add=True)



