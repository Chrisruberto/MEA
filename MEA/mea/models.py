from django.db import models

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
    desc = models.CharField(max_length=150, verbose_name='Descripcion')
    color = models.CharField(max_length=150, verbose_name='Color')
    cantidad = models.IntegerField( verbose_name='Cantidad Disponible')
    peso_neto = models.CharField(max_length=50, verbose_name='Peso neto, ml/gr')
    codigo = models.BigIntegerField( verbose_name='Código')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')


    class Meta:
        verbose_name = 'MEA'
        verbose_name_plural = 'MEA'

    def __str__(self):
        return str(self.nombre_producto)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre del Cliente')
    telefono = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return str(self.nombre)
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.CASCADE)
    productos = models.ManyToManyField(MEA, verbose_name=('Prodcutos'))
    pago = models.BooleanField(default=True)
    nota = models.CharField(max_length=150, blank=True)
    fecha = models.DateTimeField(auto_created=True,verbose_name='Fecha del pedido')
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return str(self.cliente)
    
    