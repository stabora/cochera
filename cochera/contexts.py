from django.core.urlresolvers import resolve
from django.conf import settings


def baseurl(request):
    return {'baseurl': settings.BASE_URL}


def appname(request):
    return {'appname': resolve(request.path).app_name}
