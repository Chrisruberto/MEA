from django.contrib import admin
from .models import Marca, MEA, Cliente, Pedido,PedidoProducto
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ['marca','nombre_producto', 'cantidad','color', 'desc', 'peso_neto', 'precio', 'codigo' ]
    list_filter = ['marca',]
    search_fields = ['nombre_producto']
    list_editable = ['precio']
        
class AdminC(admin.ModelAdmin):
    list_display = ['nombre','telefono']

class AdminP(admin.ModelAdmin):
    list_display = ['cliente','fecha','pago','nota']
    search_fields = ['cliente']

class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    extra = 1
    exclude = ('precio',)
    readonly_fields = ('get_precio_total_display',)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'pago', 'nota', 'fecha', 'entregado', 'precio_total']
    search_fields = ['cliente__nombre']
    inlines = [PedidoProductoInline]
    

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Marca)
admin.site.register(MEA,Admin)
admin.site.register(Cliente,AdminC)
