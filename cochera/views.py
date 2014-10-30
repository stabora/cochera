# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context, loader
from django.conf import settings
from datetime import date
from .models import Lugar, Pago, Contacto


def tabla(request, anio):
    anio_actual = date.today().year

    if not anio:
        anio = request.GET.get('anio', anio_actual)

    anio = int(anio)

    lugares = Lugar.objects.values('numero', 'id', 'titular__apellido', 'titular__id', 'titular__nombres', 'fecha_ocupacion')
    pagos = {}

    for lugar in lugares:
        pagos_lugar = {}

        for periodo in range(1, 13):
            pagos_lugar.update({int(periodo): Pago.objects.filter(lugar_id=lugar['id'], periodo__year=anio, periodo__month=periodo).values('importe', 'id', 'fecha_pago').first()})

        titular_contactos = Contacto.objects.filter(titular_id=lugar['titular__id']).values_list('valor')

        titular_datos = u'Titular: {} {}<br>Contactos: {}<br>Desde: {}'.format(
            lugar['titular__nombres'] if lugar['titular__nombres'] else 'Desocupado',
            lugar['titular__apellido'] if lugar['titular__apellido'] else '',
            ', '.join([item[0] for item in titular_contactos]),
            lugar['fecha_ocupacion'].strftime('%d/%m/%Y') if lugar['fecha_ocupacion'] else 'n/d'
        )

        pagos.update({
            int(lugar['numero']): {
                'datos': {'lugar_id': lugar['id'], 'titular': titular_datos},
                'periodos': pagos_lugar
            }
        })

    template = loader.get_template('cochera/tabla.html')

    context = Context({
        'base_url': settings.BASE_URL,
        'title': 'Pagos {}'.format(anio),
        'anio': anio,
        'rango_anios': range(anio_actual - 5, anio_actual + 1),
        'pagos': pagos,
    })

    return HttpResponse(template.render(context))
