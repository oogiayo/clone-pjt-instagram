from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def processed_timesince(value):
    dif = int((timezone.now() - value).seconds)
    unit = {'초': 60, '분': 60, '시간': 24, '일': 31, '달': 12}
    for key, val in unit.items():
        if dif//val == 0:
            return str(dif) + key
        else:
            dif //= val
    return str(dif) + '년'
