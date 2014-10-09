# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0012_auto_20141006_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='calle',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='codigo_postal',
            field=models.CharField(max_length=10, verbose_name=b'C\xc3\xb3digo postal', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='localidad',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='numero',
            field=models.IntegerField(verbose_name=b'N\xc3\xbamero', blank=True),
        ),
    ]
