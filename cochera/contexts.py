from django.conf import settings


def baseurl(request):
    return {'baseurl': settings.BASE_URL}


def appname(request):
    return {'appname': request.resolver_match.app_name}
