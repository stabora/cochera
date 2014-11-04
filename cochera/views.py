# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db.models import Sum
from django.contrib.humanize.templatetags import humanize
from datetime import date
from .models import Lugar, Contacto, Pago, Gasto, Parametro


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

        titular_datos = (
            u'Titular: {} {}<br>'
            'Desde: {}'
            '<br>Contactos: {}'
        ).format(
            lugar['titular__nombres'] if lugar['titular__nombres'] else 'Desocupado',
            lugar['titular__apellido'] if lugar['titular__apellido'] else '',
            lugar['fecha_ocupacion'].strftime('%d/%m/%Y') if lugar['fecha_ocupacion'] else 'n/d',
            ', '.join([item[0] for item in titular_contactos]),
        )

        pagos.update({
            int(lugar['numero']): {
                'datos': {'lugar_id': lugar['id'], 'titular': titular_datos},
                'periodos': pagos_lugar
            }
        })

    total_pagos = Pago.objects.aggregate(Sum('importe'))['importe__sum']
    total_gastos = Gasto.objects.exclude(categoria=3).aggregate(Sum('importe'))['importe__sum']
    total_retiros = Gasto.objects.filter(categoria=3).aggregate(Sum('importe'))['importe__sum']

    template = loader.get_template('cochera/tabla.html')

    context = RequestContext(request, {
        'title': 'Pagos {}'.format(anio),
        'anio': anio,
        'rango_anios': range(anio_actual - 5, anio_actual + 1),
        'pagos': pagos,
        'total_pagos': humanize.intcomma(total_pagos),
        'total_gastos': humanize.intcomma(total_gastos),
        'total_retiros': humanize.intcomma(total_retiros),
        'total': humanize.intcomma(total_pagos - total_gastos - total_retiros),
    })

    return HttpResponse(template.render(context))


def plano(request):
    lugares = Lugar.objects.all()

    template = loader.get_template('cochera/plano.html')
    context = RequestContext(request, {
        'title': 'Plano',
        'lugares': lugares,
        'meses_alerta_atraso': int(Parametro.objects.get(nombre='MESES_ALERTA_ATRASO_COCHERA').valor),
    })

    return HttpResponse(template.render(context))
