# -*- coding: utf-8 -*-

from django.forms import ModelForm, widgets
from cochera.models import Pago, Parametro
from cochera.widgets import MonthYearWidget


class PagoForm(ModelForm):

    class Meta:
        model = Pago
        fields = '__all__'

        try:
            importe = Parametro.objects.get(nombre='IMPORTE_ALQUILER_COCHERA').valor
        except:
            importe = None

        widgets = {
            'importe': widgets.NumberInput(attrs={'value': importe, 'step': '50.00'}),
            'periodo': MonthYearWidget()
        }
