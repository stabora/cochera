# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ValidationError
from django.utils.html import format_html
from datetime import date
from dateutil.relativedelta import relativedelta


class Parametro(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField('Descripción', max_length=200)
    valor = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Parámetro'


class Titular(models.Model):
    apellido = models.CharField(max_length=200)
    nombres = models.CharField(max_length=200)
    calle = models.CharField(max_length=100, blank=True, null=True)
    numero = models.IntegerField('Número', blank=True, null=True)
    codigo_postal = models.CharField('Código postal', max_length=10, blank=True, null=True)
    localidad = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return u'{}, {}'.format(
            self.apellido,
            self.nombres
        )

    def get_edit_link(self):
        return format_html(u'<a href="/{}/{}/{}">{}</a>'.format(
            self._meta.app_label,
            self._meta.model_name,
            self.pk,
            self
        ))

    get_edit_link.admin_order_field = 'titular__apellido'
    get_edit_link.allow_tags = True
    get_edit_link.short_description = 'Titular'

    def get_edit_links_lugares(self):
        return ', '.join([u'<a href="/{}/{}/{}">{}</a>'.format(
            lugar._meta.app_label,
            lugar._meta.module_name,
            lugar.pk,
            lugar.numero,
        ) for lugar in Lugar.objects.filter(titular_id=self.pk)])

    get_edit_links_lugares.short_description = 'Lugares'
    get_edit_links_lugares.allow_tags = True

    def get_contactos(self):
        return '<br/>'.join([str(contacto) for contacto in Contacto.objects.filter(titular_id=self.pk)])

    get_contactos.short_description = 'Contactos'
    get_contactos.allow_tags = True

    def get_vehiculos(self):
        return '<br/>'.join([str(vehiculo) for vehiculo in Vehiculo.objects.filter(titular_id=self.pk)])

    get_vehiculos.short_description = 'Vehículos'
    get_vehiculos.allow_tags = True

    def get_domicilio(self):
        if self.calle:
            return u'{} {} {} {}'.format(
                self.calle,
                str(self.numero) if self.numero else '',
                '- (' + self.codigo_postal + ')' if self.codigo_postal else '',
                self.localidad
            )
        else:
            return None

    get_domicilio.short_description = 'Domicilio'
    get_domicilio.allow_tags = True

    class Meta:
        verbose_name_plural = 'Titulares'
        ordering = ['apellido', 'nombres']


class TipoContacto(models.Model):
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
        return u'{}'.format(self.descripcion)


class Contacto(models.Model):
    tipo = models.ForeignKey('TipoContacto')
    valor = models.CharField(max_length=210)
    titular = models.ForeignKey('Titular')

    def __unicode__(self):
        return u'{}: {}'.format(
            self.tipo,
            self.valor
        )


class Vehiculo(models.Model):
    descripcion = models.CharField('Descripción', max_length=200, null=True, blank=True)
    dominio = models.CharField(max_length=20, null=True, blank=True)
    titular = models.ForeignKey(Titular)

    def __unicode__(self):
        return u'{} {}'.format(
            '[' + self.dominio + ']' if self.dominio else '',
            self.descripcion
        )

    class Meta:
        verbose_name = 'Vehículo'


class Lugar(models.Model):
    numero = models.PositiveIntegerField('número', default=0)
    titular = models.ForeignKey('Titular', null=True, blank=True, verbose_name='Titular')
    fecha_ocupacion = models.DateField('Fecha de ocupación', null=True, blank=True)

    def __unicode__(self):
        if self.titular:
            titular = self.titular
        else:
            titular = 'Desocupado'

        return u'#{}: {}'.format(
            self.numero,
            titular
        )

    def get_ocupado(self):
        if self.titular:
            return True
        else:
            return False

    get_ocupado.boolean = True
    get_ocupado.short_description = 'Ocupado'

    def get_ultimo_pago(self):
        ultimo_pago = Pago.objects.filter(lugar_id=self.id).order_by('-periodo').first()

        if ultimo_pago:
            return '<a href="/{}/pago/?lugar__id__exact={}">{}</a> ({}) - ${} {}'.format(
                self._meta.app_label,
                self.pk,
                ultimo_pago.periodo.strftime('%m/%Y'),
                ultimo_pago.titular,
                ultimo_pago.importe,
                '[P]' if ultimo_pago.parcial else ''
            )
        else:
            return ''

    get_ultimo_pago.allow_tags = True
    get_ultimo_pago.short_description = 'Último pago'

    def get_meses_atraso(self):
        ultimo_pago = Pago.objects.filter(lugar_id=self.id).order_by('-periodo').first()

        if self.titular and ultimo_pago:
            return relativedelta(date.today(), ultimo_pago.periodo).months
        else:
            return ''

    get_meses_atraso.short_description = 'Atraso (meses)'

    def get_edit_link(self):
        return format_html(u'<a href="/{}/{}/{}">{}</a>'.format(
            self._meta.app_label,
            self._meta.model_name,
            self.pk,
            self.numero
        ))

    get_edit_link.short_description = 'Lugar'
    get_edit_link.admin_order_field = 'numero'
    get_edit_link.allow_tags = True

    def get_edit_link_titular(self):
        if self.titular:
            return self.titular.get_edit_link()
        else:
            return 'Desocupado'

    get_edit_link_titular.admin_order_field = 'titular__apellido'
    get_edit_link_titular.short_description = 'Titular'

    class Meta:
        verbose_name_plural = 'Lugares'
        ordering = ['numero']


class Pago(models.Model):
    lugar = models.ForeignKey('Lugar')
    titular = models.ForeignKey('Titular')
    periodo = models.DateField('Período')
    fecha_pago = models.DateField('Fecha de pago')
    importe = models.DecimalField(max_digits=13, decimal_places=2)
    parcial = models.BooleanField(default=False)
    comentario = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'#{} {} - {} - ${}'.format(
            self.lugar.numero,
            self.titular,
            self.periodo.strftime('%m/%Y'),
            self.importe
        )

    def clean(self):
        if hasattr(self, 'lugar'):
            if self.lugar.titular is None and not hasattr(self, 'titular'):
                raise ValidationError(u'El lugar se encuentra desocupado')

            if self.pk is None and self.check_periodo_pago():
                raise ValidationError(u'Ya se ingresó un pago para el lugar y el período seleccionados')

    def save(self, *args, **kwargs):
        if not hasattr(self, 'titular'):
            self.titular = Titular.objects.get(pk=self.lugar.titular.pk)

        super(Pago, self).save(*args, **kwargs)

    def check_periodo_pago(self):
        return Pago.objects.filter(lugar=self.lugar.pk, periodo=self.periodo, parcial=False).exists()

    def get_lugar_numero(self):
        return self.lugar.numero

    get_lugar_numero.short_description = 'Lugar'

    def get_edit_link_lugar(self):
        return self.lugar.get_edit_link()

    get_edit_link_lugar.short_description = 'Lugar'
    get_edit_link_lugar.admin_order_field = 'lugar'

    def get_edit_link_titular(self):
        return self.titular.get_edit_link()

    get_edit_link_titular.short_description = 'Titular'
    get_edit_link_titular.admin_order_field = 'titular__apellido'


class CategoriaGasto(models.Model):
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Categoría de gasto'
        verbose_name_plural = 'Categorías de gastos'
        ordering = ['descripcion']


class Gasto(models.Model):
    categoria = models.ForeignKey('CategoriaGasto')
    fecha = models.DateField()
    importe = models.DecimalField(max_digits=13, decimal_places=2)
    comentario = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '({}) {}: ${}'.format(
            self.fecha.strftime('%d/%m/%Y'),
            self.categoria,
            self.importe
        )
