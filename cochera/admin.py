# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from cochera.models import Titular, Contacto, Vehiculo, Lugar, Pago, CategoriaGasto, Gasto, Parametro
from cochera.forms import PagoForm


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
    list_display = ['__unicode__', 'get_link_lugares', 'get_contactos', 'get_domicilio', 'get_vehiculos']
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


class PagoAdmin(admin.ModelAdmin):
    list_display = [
        'get_lugar_numero', 'get_link_titular', 'fecha_pago',
        'get_periodo', 'importe', 'parcial', 'comentario'
    ]
    list_filter = ['titular', 'periodo', 'parcial']
    ordering = ['-fecha_pago']
    search_fields = ['titular__apellido', 'titular__nombres']
    form = PagoForm


class GastoAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'categoria', 'importe', 'comentario']
    list_filter = ['categoria', 'fecha']
    ordering = ['-fecha']
    search_fields = ['comentario']


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


class LugarAdmin(admin.ModelAdmin):
    list_display = ['numero', 'get_link_titular', 'fecha_ocupado', 'ocupado']
    list_filter = [LugarOcupacionFilter, 'titular', 'fecha_ocupado']
    ordering = ['numero']
    search_fields = ['titular__apellido', 'titular__nombres']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(LugarAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


admin.site.register(Titular, TitularAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(CategoriaGasto)
admin.site.register(Gasto, GastoAdmin)
admin.site.register(Parametro, ParametroAdmin)
