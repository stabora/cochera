# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0009_auto_20141005_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoContacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tipo',
            field=models.ForeignKey(to='cochera.TipoContacto'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='fecha_ocupado',
            field=models.DateField(null=True, verbose_name=b'Fecha de ocupaci\xc3\xb3n', blank=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='numero',
            field=models.PositiveIntegerField(default=0, verbose_name=b'n\xc3\xbamero'),
        ),
    ]
