# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0011_vehiculo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'verbose_name': 'Veh\xedculo'},
        ),
        migrations.AddField(
            model_name='persona',
            name='calle',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='persona',
            name='codigo_postal',
            field=models.CharField(max_length=10, null=True, verbose_name=b'C\xc3\xb3digo postal'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='persona',
            name='localidad',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='persona',
            name='numero',
            field=models.IntegerField(null=True, verbose_name=b'N\xc3\xbamero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='descripcion',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Descripci\xc3\xb3n'),
        ),
    ]
