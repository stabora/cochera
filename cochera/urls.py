# -*- coding: utf:8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'cochera',
    url(r'^tabla/(?P<anio>\d{4})?', 'views.tabla'),
    url(r'^plano/', 'views.plano'),
)
