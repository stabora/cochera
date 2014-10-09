# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0020_auto_20141006_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='titular',
            field=models.ForeignKey(blank=True, to='cochera.Persona', null=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='titular',
            field=models.ForeignKey(blank=True, to='cochera.Persona', null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='calle',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='codigo_postal',
            field=models.CharField(max_length=10, null=True, verbose_name=b'C\xc3\xb3digo postal', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='localidad',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='numero',
            field=models.IntegerField(null=True, verbose_name=b'N\xc3\xbamero', blank=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='descripcion',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='dominio',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
