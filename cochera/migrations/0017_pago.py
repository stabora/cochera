# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0016_auto_20141006_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodo', models.DateField()),
                ('fecha_pago', models.DateField()),
                ('lugar', models.ForeignKey(to='cochera.Lugar')),
                ('persona', models.ForeignKey(to='cochera.Persona')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
