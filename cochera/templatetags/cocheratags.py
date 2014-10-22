from django import template
from django.contrib.admin.templatetags.admin_list import results, result_headers

register = template.Library()


def result_list(cl):
    total = 0

    for item in cl.result_list:
        total += item.importe

    return {
        'cl': cl,
        'result_headers': list(result_headers(cl)),
        'results': list(results(cl)),
        'extra': total
    }

register.inclusion_tag('admin/cochera/gasto/change_list_results.html')(result_list)
