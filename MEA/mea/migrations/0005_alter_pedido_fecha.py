# Generated by Django 4.2 on 2023-04-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mea', '0004_remove_pedido_pedido_pedido_productos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(auto_created=True, verbose_name='Fecha del pedido'),
        ),
    ]