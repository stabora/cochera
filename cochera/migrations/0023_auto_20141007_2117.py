# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0022_auto_20141007_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titular',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apellido', models.CharField(max_length=200)),
                ('nombres', models.CharField(max_length=200)),
                ('calle', models.CharField(max_length=100, null=True, blank=True)),
                ('numero', models.IntegerField(null=True, verbose_name=b'N\xc3\xbamero', blank=True)),
                ('codigo_postal', models.CharField(max_length=10, null=True, verbose_name=b'C\xc3\xb3digo postal', blank=True)),
                ('localidad', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Titulares',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='titular',
            field=models.ForeignKey(to='cochera.Titular'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='titular',
            field=models.ForeignKey(verbose_name=b'Titular', blank=True, to='cochera.Titular', null=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='titular',
            field=models.ForeignKey(blank=True, to='cochera.Titular', null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='titular',
            field=models.ForeignKey(to='cochera.Titular'),
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]
