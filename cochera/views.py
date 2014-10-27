from django.http import HttpResponse
from django.template import Context, loader
from django.conf import settings
from datetime import date
from .models import Lugar, Pago


def tabla(request, anio=date.today().year):
    lugares = Lugar.objects.values('numero')
    periodos = ()
    pagos = {
        '1': {'1': True, '2': False, '3': True, '4': True, '5': True, '6': True, '7': True, '8': True, '9': True, '10': True, '11': True, '12': True}
    }

    for periodo in range(1, 12):
        periodos += ('{}/{}'.format(periodo, anio),)

    for lugar in lugares:
        for periodo in periodos:
            pass

    template = loader.get_template('cochera/tabla.html')

    context = Context({
        'base_url': settings.BASE_URL,
        'title': 'Pagos {}'.format(anio),
        'anio': anio,
        'periodos': periodos,
        'lugares': lugares,
        'pagos': pagos,
    })

    return HttpResponse(template.render(context))
