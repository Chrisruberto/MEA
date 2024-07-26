from django.db import models
from django_cryptography.fields import encrypt
from django.utils.html import format_html

# Create your models here.

class Relacion(models.Model):
    nombre = models.CharField(max_length=150)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.nombre 
    
class Marca(Relacion):
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        
class MEA(models.Model):
    nombre_producto = models.CharField(max_length=150, verbose_name='Nombre del Producto')
    marca = models.ForeignKey(Marca, verbose_name='Marca', on_delete=models.CASCADE)
    desc = models.CharField(max_length=150, verbose_name='Descripcion',blank=True, null=True)
    color = models.CharField(max_length=150, verbose_name='Color',blank=True, null=True)
    aroma = models.CharField(max_length=150, verbose_name='Aroma',blank=True, null=True)
    cantidad = models.IntegerField( verbose_name='Cantidad Disponible',blank=True, null=True)
    peso_neto = models.CharField(max_length=50, verbose_name='Peso neto, ml/gr',blank=True, null=True)
    codigo = models.BigIntegerField( verbose_name='Código',blank=True,null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')


    class Meta:
        verbose_name = 'MEA'
        verbose_name_plural = 'MEA'

    def __str__(self):
        return str(self.nombre_producto)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre del Cliente')
    telefono = encrypt(models.CharField(max_length=150))
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return str(self.nombre)
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pago = models.DecimalField(max_digits=10, decimal_places=2)
    nota = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=False)

    def precio_total(self):
        # Verificar el precio total de todos los productos en el pedido
        total = sum(pp.get_precio_total() for pp in self.productos.all())
        return total

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente}'
    
class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='productos', on_delete=models.CASCADE)
    producto = models.ForeignKey(MEA, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio', blank=True, null=True)

    class Meta:
        verbose_name = 'Pedido Producto'
        verbose_name_plural = 'Pedidos Productos'

    def save(self, *args, **kwargs):
        # Asignar el precio del producto automáticamente
        self.precio = self.producto.precio

        # Llamar al método save del modelo base
        super().save(*args, **kwargs)

        # Descontar la cantidad del producto en MEA
        if self.producto.cantidad is not None:
            if self.producto.cantidad >= self.cantidad:
                self.producto.cantidad -= self.cantidad
                self.producto.save()
            else:
                raise ValueError('La cantidad solicitada excede la cantidad disponible.')
    

    def get_precio_total(self):
        # Verificar que precio y cantidad no sean None
        if self.precio is not None and self.cantidad is not None:
            return self.precio * self.cantidad
        return 0  # O un valor predeterminado adecuado
    
    def get_precio_total_display(self):
        # Método para mostrar el precio total con formato en la administración
        return format_html(f'${self.get_precio_total():,.2f}')

    def delete(self, *args, **kwargs):
        # Antes de eliminar, sumar la cantidad al producto en MEA
        if self.producto.cantidad is not None:
            self.producto.cantidad += self.cantidad
            self.producto.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'{self.producto} - {self.cantidad}'
    