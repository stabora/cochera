# -*- coding: utf:8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'cochera',
    url(r'^tabla/(?P<anio>\d+)?', 'views.tabla'),
)
