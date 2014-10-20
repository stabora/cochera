# -*- coding: utf-8 -*-

from datetime import datetime
from django.forms import ModelForm, widgets
from cochera.models import Pago, Gasto, Parametro
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
        self.fields['fecha_pago'].initial = datetime.today()

    class Meta:
        model = Pago
        exclude = ('titular',)

        widgets = {
            'importe': widgets.NumberInput(attrs={'step': '10.00'}),
            'periodo': MonthYearWidget()
        }


class GastoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(GastoForm, self).__init__(*args, **kwargs)

        self.fields['fecha'].initial = datetime.today()

    class Meta:
        model = Gasto
        fields = '__all__'

        widgets = {
            'importe': widgets.NumberInput(attrs={'step': '0.10'}),
        }
