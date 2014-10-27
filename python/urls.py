# -*- coding: utf:8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^', include(admin.site.urls)),
    url(r'^', include('cochera.urls')),
)

admin.site.site_header = 'Cochera - Administración'
admin.site.site_title = 'Cochera - Administración'
