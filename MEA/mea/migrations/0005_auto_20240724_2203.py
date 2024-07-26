# Generated by Django 3.2.7 on 2024-07-24 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mea', '0004_alter_pedidoproducto_precio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={},
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mea.cliente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='entregado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='nota',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='pago',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]