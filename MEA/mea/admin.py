from django.contrib import admin
from django import forms
from .models import Marca, MEA, Cliente, Pedido,PedidoProducto
from django.contrib import admin, messages
from django.core.exceptions import ValidationError
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
    extra = 0
    exclude = ('precio',)
    readonly_fields = ('get_precio_total_display',)

    def save_formset(self, request, form, formset, change):
        # Validar los formularios del formset
        for form in formset.forms:
            if form.is_valid():
                try:
                    form.instance.clean()
                except ValidationError as e:
                    form._errors[forms.forms.NON_FIELD_ERRORS] = forms.utils.ErrorList([str(e)])

        super().save_formset(request, form, formset, change)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'pago', 'nota', 'fecha', 'entregado', 'precio_total']
    search_fields = ['cliente__nombre']
    inlines = [PedidoProductoInline]
    

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Marca)
admin.site.register(MEA,Admin)
admin.site.register(Cliente,AdminC)
