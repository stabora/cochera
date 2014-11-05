# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.humanize.templatetags import humanize
from django.db.models import Sum
from datetime import date
from dateutil.relativedelta import relativedelta
from cochera.models import Titular, Contacto, Vehiculo, Lugar, Pago, CategoriaGasto, Gasto, Parametro
from cochera.forms import PagoForm, GastoForm


class ParametroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'valor']
    ordering = ['nombre']
    search_fields = ['nombre', 'descripcion']


class ContactoInline(admin.TabularInline):
    model = Contacto
    extra = 2
    suit_classes = 'suit-tab suit-tab-general'


class VehiculoInline(admin.TabularInline):
    fieldsets = [
        (None, {'fields': ['dominio', 'descripcion']}),
    ]
    model = Vehiculo
    extra = 1
    suit_classes = 'suit-tab suit-tab-avanzado'


class TitularAsignacionFilter(SimpleListFilter):
    title = 'Estado'
    parameter_name = 'estado'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Asignados'),
            ('2', 'No asignados'),
        )

    def queryset(self, request, queryset):
        lugares = Lugar.objects.exclude(titular=None).values_list('titular')

        if self.value() == '1':
            return queryset.filter(pk__in=lugares)
        elif self.value() == '2':
            return queryset.exclude(pk__in=lugares)
        else:
            return queryset


class TitularAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'get_edit_links_lugares', 'get_contactos', 'get_domicilio', 'get_vehiculos']
    suit_form_tabs = (('general', 'General'), ('avanzado', 'Avanzado'))
    fieldsets = [
        (None, {
            'fields': ['apellido', 'nombres'],
            'classes': ('suit-tab', 'suit-tab-general')
        }),
        ('Domicilio postal', {
            'fields': ['calle', 'numero', 'codigo_postal', 'localidad'],
            'classes': ('suit-tab', 'suit-tab-avanzado')
        }),
    ]
    list_filter = [TitularAsignacionFilter]
    search_fields = ['apellido', 'nombres']
    inlines = [ContactoInline, VehiculoInline]
    ordering = ['apellido', 'nombres']


class PagoPeriodoFilter(SimpleListFilter):
    title = 'Período'
    parameter_name = 'periodo'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Este mes'),
            ('2', 'El mes pasado'),
            ('3', 'Los últimos 3 meses'),
            ('4', 'Los últimos 6 meses'),
            ('5', 'Este año'),
            ('6', 'El año pasado'),
        )

    def queryset(self, request, queryset):
        fecha_actual = date.today()

        if self.value() == '1':
            fecha_desde = fecha_actual
            return queryset.filter(periodo=date(fecha_desde.year, fecha_desde.month, 1))
        elif self.value() == '2':
            fecha_desde = fecha_actual + relativedelta(months=-1)
            return queryset.filter(periodo=date(fecha_desde.year, fecha_desde.month, 1))
        elif self.value() == '3':
            fecha_desde = fecha_actual + relativedelta(months=-2)
            return queryset.filter(periodo__gte=date(fecha_desde.year, fecha_desde.month, 1))
        elif self.value() == '4':
            fecha_desde = fecha_actual + relativedelta(months=-5)
            return queryset.filter(periodo__gte=date(fecha_desde.year, fecha_desde.month, 1))
        elif self.value() == '5':
            fecha_desde = date(fecha_actual.year, 1, 1)
            return queryset.filter(periodo__year=fecha_desde.year)
        elif self.value() == '6':
            fecha_desde = fecha_actual + relativedelta(years=-1)
            return queryset.filter(periodo__year=fecha_desde.year)
        else:
            return queryset


class PagoAdmin(admin.ModelAdmin):
    list_display = [
        'get_periodo', 'get_edit_link_lugar', 'get_edit_link_titular', 'get_fecha_pago',
        'get_importe', 'parcial', 'comentario'
    ]
    list_filter = ['lugar', 'titular', PagoPeriodoFilter, 'parcial']
    ordering = ['-fecha_pago', '-periodo']
    search_fields = ['lugar__numero', 'titular__apellido', 'titular__nombres']
    form = PagoForm

    def changelist_view(self, request, extra_context=None):
        response = super(PagoAdmin, self).changelist_view(request, extra_context)

        try:
            filtered_qs = response.context_data['cl'].query_set
        except KeyError:
            pass

        total_pagos = Pago.objects.aggregate(Sum('importe'))['importe__sum']
        total_gastos = Gasto.objects.exclude(categoria=3).aggregate(Sum('importe'))['importe__sum']
        total_retiros = Gasto.objects.filter(categoria=3).aggregate(Sum('importe'))['importe__sum']

        extra_context = {
            'total_pagos': humanize.intcomma(total_pagos),
            'total_gastos': humanize.intcomma(total_gastos),
            'total_retiros': humanize.intcomma(total_retiros),
            'total': humanize.intcomma(total_pagos - total_gastos - total_retiros),
            'total_filtrado': humanize.intcomma(filtered_qs.aggregate(Sum('importe'))['importe__sum']) if response.context_data.get('preserved_filters') else 0,
        }

        return super(PagoAdmin, self).changelist_view(request, extra_context=extra_context)

    def add_view(self, request, extra_context=None):
        extra_context = {
            'IMPORTE_ALQUILER_COCHERA': int(Parametro.objects.get(nombre='IMPORTE_ALQUILER_COCHERA').valor),
            'IMPORTE_ALQUILER_OFICINA': int(Parametro.objects.get(nombre='IMPORTE_ALQUILER_OFICINA').valor),
        }

        return super(PagoAdmin, self).add_view(request, extra_context=extra_context)

    def get_importe(self, obj):
        return humanize.intcomma(obj.importe)

    get_importe.short_description = 'Importe'
    get_importe.admin_order_field = 'importe'

    def get_fecha_pago(self, obj):
        return obj.fecha_pago.strftime('%d/%m/%Y')

    get_fecha_pago.short_description = 'Fecha de pago'
    get_fecha_pago.admin_order_field = 'fecha_pago'

    def get_periodo(self, obj):
        return obj.periodo.strftime('%m/%Y')

    get_periodo.short_description = 'Período de pago'
    get_periodo.admin_order_field = 'periodo'


class GastoAdmin(admin.ModelAdmin):
    list_display = ['categoria', 'get_fecha', 'get_importe', 'comentario']
    list_filter = ['categoria', 'fecha']
    ordering = ['-fecha']
    search_fields = ['categoria__descripcion', 'comentario']
    form = GastoForm

    def changelist_view(self, request, extra_context=None):
        response = super(GastoAdmin, self).changelist_view(request, extra_context)

        try:
            filtered_qs = response.context_data['cl'].query_set
        except KeyError:
            pass

        total_pagos = Pago.objects.aggregate(Sum('importe'))['importe__sum']
        total_gastos = Gasto.objects.exclude(categoria=3).aggregate(Sum('importe'))['importe__sum']
        total_retiros = Gasto.objects.filter(categoria=3).aggregate(Sum('importe'))['importe__sum']

        extra_context = {
            'total_pagos': humanize.intcomma(total_pagos),
            'total_gastos': humanize.intcomma(total_gastos),
            'total_retiros': humanize.intcomma(total_retiros),
            'total': humanize.intcomma(total_pagos - total_gastos - total_retiros),
            'total_filtrado': humanize.intcomma(filtered_qs.aggregate(Sum('importe'))['importe__sum']) if response.context_data.get('preserved_filters') else 0,
        }

        return super(GastoAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_importe(self, obj):
        return humanize.intcomma(obj.importe)

    get_importe.short_description = 'Importe'
    get_importe.admin_order_field = 'importe'

    def get_fecha(self, obj):
        return obj.fecha.strftime('%d/%m/%Y')

    get_fecha.short_description = 'Fecha'
    get_fecha.admin_order_field = 'fecha'


class LugarOcupacionFilter(SimpleListFilter):
    title = 'Estado'
    parameter_name = 'estado'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Ocupados'),
            ('2', 'Desocupados'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.exclude(titular=None)
        elif self.value() == '2':
            return queryset.filter(titular=None)
        else:
            return queryset


class LugarFechaOcupacionFilter(SimpleListFilter):
    title = 'Fecha de ocupación'
    parameter_name = 'fecha_ocupacion'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Este mes'),
            ('2', 'El mes pasado'),
            ('3', 'Los últimos 3 meses'),
            ('4', 'Los últimos 6 meses'),
            ('5', 'Este año'),
            ('6', 'El año pasado'),
        )

    def queryset(self, request, queryset):
        fecha_actual = date.today()

        if self.value() == '1':
            fecha_desde = fecha_actual
            return queryset.filter(fecha_ocupacion=date(fecha_desde.year, fecha_desde.month, 1))
        elif self.value() == '2':
            fecha_desde = fecha_actual + relativedelta(months=-1)
            return queryset.filter(fecha_ocupacion=date(fecha_desde.year, fecha_desde.month, 1))
        elif self.value() == '3':
            fecha_desde = fecha_actual + relativedelta(months=-2)
            return queryset.filter(fecha_ocupacion__gte=date(fecha_desde.year, fecha_desde.month, 1))
        elif self.value() == '4':
            fecha_desde = fecha_actual + relativedelta(months=-5)
            return queryset.filter(fecha_ocupacion__gte=date(fecha_desde.year, fecha_desde.month, 1))
        elif self.value() == '5':
            fecha_desde = date(fecha_actual.year, 1, 1)
            return queryset.filter(periodo__year=fecha_desde.year)
        elif self.value() == '6':
            fecha_desde = fecha_actual + relativedelta(years=-1)
            return queryset.filter(periodo__year=fecha_desde.year)
        else:
            return queryset


class LugarAdmin(admin.ModelAdmin):
    list_display = [
        'numero', 'get_edit_link_titular', 'fecha_ocupacion',
        'get_ultimo_pago', 'get_ocupado', 'get_meses_atraso'
    ]
    list_filter = [LugarOcupacionFilter, 'titular', LugarFechaOcupacionFilter]
    ordering = ['numero']
    search_fields = ['numero', 'titular__apellido', 'titular__nombres']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(LugarAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def get_meses_atraso(self, obj):
        meses_atraso = obj.get_meses_atraso()

        if meses_atraso > int(Parametro.objects.get(nombre='MESES_ALERTA_ATRASO_COCHERA').valor):
            return '<span style="color: Red">{}</style>'.format(
                meses_atraso
            )
        else:
            return meses_atraso

    get_meses_atraso.short_description = 'Atraso (meses)'
    get_meses_atraso.allow_tags = True


admin.site.register(Titular, TitularAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(CategoriaGasto)
admin.site.register(Gasto, GastoAdmin)
admin.site.register(Parametro, ParametroAdmin)
