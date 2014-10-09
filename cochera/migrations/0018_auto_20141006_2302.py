# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0017_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='fecha_pago',
            field=models.DateField(verbose_name=b'Fecha de pago'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='periodo',
            field=models.DateField(verbose_name=b'Per\xc3\xadodo'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='persona',
            field=models.ForeignKey(default=None, blank=True, to='cochera.Persona', null=True),
        ),
    ]
