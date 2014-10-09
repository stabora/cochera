# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0010_auto_20141006_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200, null=True)),
                ('dominio', models.CharField(max_length=20, null=True)),
                ('persona', models.ForeignKey(to='cochera.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
