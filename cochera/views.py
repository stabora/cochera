from django.http import HttpResponse
from django.template import Context, loader
from django.conf import settings
from datetime import date
from .models import Lugar, Pago


def tabla(request, anio):
    if not anio:
        anio = date.today().year

    lugares = Lugar.objects.values('numero', 'id')
    pagos = {}

    for lugar in lugares:
        pagos_lugar = {}

        for periodo in range(1, 13):
            pagos_lugar.update({int(periodo): Pago.objects.filter(lugar_id=lugar['id'], periodo__year=anio, periodo__month=periodo).values('importe', 'id').first()})

        pagos.update({int(lugar['numero']): pagos_lugar})

    template = loader.get_template('cochera/tabla.html')

    context = Context({
        'base_url': settings.BASE_URL,
        'title': 'Pagos {}'.format(anio),
        'anio': anio,
        'pagos': pagos,
    })

    return HttpResponse(template.render(context))
