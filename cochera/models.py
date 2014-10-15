# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ValidationError
from django.template.defaultfilters import date as _date


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

    def get_contactos(self):
        return '<br/>'.join([str(contacto) for contacto in Contacto.objects.filter(titular_id=self.pk)])

    get_contactos.short_description = 'Contactos'
    get_contactos.allow_tags = True

    def get_lugares(self):
        return ', '.join([u'<a href="/admin/{}/{}/{}">{}</a>'.format(
            lugar._meta.app_label,
            lugar._meta.module_name,
            lugar.pk,
            lugar.numero,
        ) for lugar in Lugar.objects.filter(titular_id=self.pk)])

    get_lugares.short_description = 'Lugares'
    get_lugares.allow_tags = True

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
    fecha_ocupado = models.DateField('Fecha de ocupación', null=True, blank=True)

    def __unicode__(self):
        if self.titular:
            titular = self.titular
        else:
            titular = 'Desocupado'

        return u'#{}: {}'.format(
            self.numero,
            titular
        )

    def ocupado(self):
        if self.titular:
            return True
        else:
            return False

    ocupado.boolean = True
    ocupado.short_description = '¿Ocupado?'

    class Meta:
        verbose_name_plural = 'Lugares'


class Pago(models.Model):
    lugar = models.ForeignKey('Lugar')
    titular = models.ForeignKey('Titular')
    periodo = models.DateField('Período')
    fecha_pago = models.DateField('Fecha de pago')
    importe = models.DecimalField(max_digits=13, decimal_places=2)
    parcial = models.BooleanField(default=False)
    comentario = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'{} - {} - ${}'.format(
            self.lugar,
            _date(self.periodo, 'E \d\e Y'),
            self.importe
        )

    def clean(self):
        if hasattr(self, 'lugar'):
            if self.lugar.titular is None:
                raise ValidationError(u'El lugar se encuentra desocupado')

            if self.periodo_pago():
                raise ValidationError(u'Ya se ingresó un pago para el lugar y el período seleccionados')

    def save(self, *args, **kwargs):
        self.titular = Titular.objects.get(pk=self.lugar.titular.pk)
        super(Pago, self).save(*args, **kwargs)

    def get_lugar_numero(self):
        return self.lugar.numero

    get_lugar_numero.short_description = 'Lugar'

    def get_periodo(self):
        return _date(self.periodo, 'E \d\e Y')

    get_periodo.short_description = 'Período de pago'
    get_periodo.admin_order_field = 'periodo'

    def periodo_pago(self):
        return Pago.objects.filter(lugar=self.lugar.pk, periodo=self.periodo).exists()


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
    importe = models.PositiveIntegerField()
    comentario = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '({}) {}: ${}'.format(
            _date(self.fecha, 'd/m/Y'),
            self.categoria,
            self.importe
        )
