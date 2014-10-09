# -*- coding: utf-8 -*-

import datetime
from django.db import models
from django.utils import timezone


class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('fecha de publicación')

    def __unicode__(self):
        return u'%s' % (self.texto)

    def publicada_recientemente(self):
        return self.fecha_publicacion >= timezone.now() - datetime.timedelta(days=1)

    publicada_recientemente.admin_order_field = 'fecha_publicacion'
    publicada_recientemente.boolean = True
    publicada_recientemente.short_description = '¿Publicada recientemente?'


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s (%s votos)' % (self.texto, self.votos)

    class Meta:
        verbose_name_plural = 'Opciones'
