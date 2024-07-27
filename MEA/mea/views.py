from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.safestring import mark_safe
import json

from decimal import Decimal


from .models import Pedido, PedidoProducto, MEA
from .models import MEA


@login_required 
def list_products(request):
    products = MEA.objects.all()
    return render(request, 'list_products.html', {'products': products})



MESES_EN_ES = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre',
}

@login_required
def cliente_venta(request):
    # Agrupar gastos por cliente y por mes
    gastos_por_cliente = Pedido.objects.values('cliente__nombre', 'fecha__year', 'fecha__month') \
        .annotate(total_gastado=Sum('pago')) \
        .order_by('cliente__nombre', 'fecha__year', 'fecha__month')

    # Calcular el total generado de todas las ventas
    total_generado = Pedido.objects.aggregate(total=Sum('pago'))['total'] or 0

    # Convertir números de meses a nombres en español
    for gasto in gastos_por_cliente:
        mes_numero = gasto['fecha__month']
        gasto['mes_nombre'] = MESES_EN_ES.get(mes_numero, 'Mes desconocido')
        gasto['total_gastado'] = float(gasto['total_gastado'])  # Convertir Decimal a float

    # Preparar datos para el gráfico
    data = {}
    for gasto in gastos_por_cliente:
        cliente = gasto['cliente__nombre']
        mes = gasto['mes_nombre']
        if cliente not in data:
            data[cliente] = {}
        data[cliente][mes] = gasto['total_gastado']

    # Organizar los datos para el gráfico
    clientes = list(data.keys())
    meses = list(MESES_EN_ES.values())
    gastos_por_mes = []
    for cliente in clientes:
        gastos_cliente = []
        for mes in meses:
            gastos_cliente.append(data[cliente].get(mes, 0))
        gastos_por_mes.append(gastos_cliente)

    # Preparar contexto para el template
    contexto = {
        'gastos_por_cliente': gastos_por_cliente,
        'total_generado': total_generado,
        'clientes': mark_safe(json.dumps(clientes)),
        'meses': mark_safe(json.dumps(meses)),
        'gastos_por_mes': mark_safe(json.dumps(gastos_por_mes)),
    }

    return render(request, 'cliente_venta.html', contexto)


