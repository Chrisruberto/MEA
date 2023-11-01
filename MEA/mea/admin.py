from django.contrib import admin
from .models import Marca, MEA, Cliente, Pedido
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ['id','marca','nombre_producto', 'cantidad','color', 'desc', 'peso_neto', 'precio', 'codigo' ]
    list_filter = ['marca',]
    search_fields = ['nombre_producto']
        
class AdminC(admin.ModelAdmin):
    list_display = ['nombre','telefono']

class AdminP(admin.ModelAdmin):
    list_display = ['cliente','fecha','pago','nota']
    search_fields = ['cliente']

admin.site.register(Marca)
admin.site.register(MEA,Admin)
admin.site.register(Cliente,AdminC)
admin.site.register(Pedido,AdminP)