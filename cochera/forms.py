# -*- coding: utf-8 -*-

from datetime import datetime
from django.forms import ModelForm, widgets
from cochera.models import Pago, Parametro
from cochera.widgets import MonthYearWidget


class PagoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        try:
            importe = Parametro.objects.get(nombre='IMPORTE_ALQUILER_COCHERA').valor
        except:
            importe = None

        super(PagoForm, self).__init__(*args, **kwargs)

        self.fields['importe'].initial = importe
        self.fields['periodo'].initial = datetime.now()
        self.fields['fecha_pago'].initial = datetime.now()

    class Meta:
        model = Pago
        exclude = ('titular',)

        widgets = {
            'importe': widgets.NumberInput(attrs={'step': '50.00'}),
            'periodo': MonthYearWidget()
        }
