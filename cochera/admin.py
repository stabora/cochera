# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import SimpleListFilter
from cochera.models import Titular, Contacto, Vehiculo, Lugar, Pago, Parametro
from cochera.forms import PagoForm


class ParametroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'valor']
    ordering = ['nombre']
    search_fields = ['nombre', 'descripcion']


class ContactoInline(admin.TabularInline):
    model = Contacto
    extra = 2


class VehiculoInline(admin.TabularInline):
    fieldsets = [
        (None, {'fields': ['dominio', 'descripcion']}),
    ]
    model = Vehiculo
    extra = 1
    classes = ['collapse']


class TitularAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'get_lugares', 'get_contactos', 'get_domicilio', 'get_vehiculos']
    fieldsets = [
        (None, {'fields': ['apellido', 'nombres']}),
        ('Domicilio postal', {'fields': ['calle', 'numero', 'codigo_postal', 'localidad'], 'classes': ['collapse']}),
    ]
    inlines = [ContactoInline, VehiculoInline]
    ordering = ['apellido', 'nombres']


class PagoAdmin(admin.ModelAdmin):
    list_display = ['get_lugar_numero', 'get_titular_edit_link', 'fecha_pago', 'periodo', 'importe']
    list_filter = ['titular', 'periodo']
    ordering = ['-fecha_pago']
    search_fields = ['titular__apellido', 'titular__nombres']
    form = PagoForm

    def get_titular_edit_link(self, obj):
        return format_html('<a href="/admin/{}/{}/{}">{}</a>'.format(
            obj.titular._meta.app_label,
            obj.titular._meta.model_name,
            obj.titular.pk,
            obj.titular
        ))

    get_titular_edit_link.admin_order_field = 'titular__apellido'
    get_titular_edit_link.allow_tags = True
    get_titular_edit_link.short_description = 'Titular'


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
    list_display = ['numero', 'get_titular_edit_link', 'fecha_ocupado', 'ocupado']
    list_filter = [LugarOcupacionFilter, 'titular', 'fecha_ocupado']
    ordering = ['numero']
    search_fields = ['titular__apellido', 'titular__nombres']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_titular_edit_link(self, obj):
        if obj.titular:
            return format_html(u'<a href="/admin/{}/{}/{}">{}</a>'.format(
                obj.titular._meta.app_label,
                obj.titular._meta.model_name,
                obj.titular.pk,
                obj.titular
            ))
        else:
            return None

    get_titular_edit_link.admin_order_field = 'titular__apellido'
    get_titular_edit_link.allow_tags = True
    get_titular_edit_link.short_description = 'Titular'


admin.site.register(Titular, TitularAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Parametro, ParametroAdmin)