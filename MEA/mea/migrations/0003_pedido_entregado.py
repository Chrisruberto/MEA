# Generated by Django 3.2.7 on 2024-07-24 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mea', '0002_auto_20240724_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='entregado',
            field=models.BooleanField(default=True),
        ),
    ]
