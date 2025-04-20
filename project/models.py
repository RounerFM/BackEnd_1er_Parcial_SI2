from django.db import models

# Create your models here.
class Roles(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

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


class Producto(models.Model):
    nombre= models.CharField(max_length=200)
    precio= models.DecimalField(max_digits=10,decimal_places=2)
    idCategorias= models.ForeignKey(Categorias,on_delete=models.CASCADE)


class Inventario(models.Model):
    stock= models.PositiveIntegerField()
    idProducto= models.ForeignKey(Producto,on_delete=models.CASCADE)
    idAlmacen= models.ForeignKey(Almacen,on_delete=models.CASCADE)

