# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(choices=[(1, b'Tel\xc3\xa9fono celular'), (2, b'Tel\xc3\xa9fono fijo'), (3, b'e-mail')])),
                ('valor', models.CharField(max_length=210)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(default=0)),
                ('fecha_ocupado', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Lugares',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apellido', models.CharField(max_length=200)),
                ('nombres', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lugar',
            name='titular',
            field=models.ForeignKey(to='cochera.Persona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contacto',
            name='persona',
            field=models.ForeignKey(to='cochera.Persona'),
            preserve_default=True,
        ),
    ]
