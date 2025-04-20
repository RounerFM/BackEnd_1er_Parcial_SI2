from django.contrib import admin
from .models import Roles, TipoDePago, Categorias, Almacen, Descuento, Producto, Inventario

admin.site.register(Roles)
admin.site.register(TipoDePago)
admin.site.register(Categorias)
admin.site.register(Almacen)
admin.site.register(Descuento)
admin.site.register(Producto)
admin.site.register(Inventario)

# Register your models here.
