# -*- coding: utf:8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'python.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

admin.site.site_header = 'Cochera - Administración'
admin.site.site_title = 'Cochera - Administración'
