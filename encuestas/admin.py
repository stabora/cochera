# -*- coding: utf-8 -*-

from django.contrib import admin
from encuestas.models import Pregunta, Opcion


class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 3


class PreguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['texto']}),
        ('Información de publicación', {'fields': ['fecha_publicacion'], 'classes': ['collapse']})
    ]
    inlines = [OpcionInline]
    list_display = ('texto', 'fecha_publicacion', 'publicada_recientemente')
    list_filter = ['fecha_publicacion']
    search_fields = ['texto']
    list_per_page = 25


admin.site.register(Pregunta, PreguntaAdmin)
