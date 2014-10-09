# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opcion',
            options={'verbose_name_plural': 'Opciones'},
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='fecha_publicacion',
            field=models.DateTimeField(verbose_name=b'fecha de publicaci\xc3\xb3n'),
        ),
    ]
