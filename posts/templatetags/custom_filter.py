from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def processed_timesince(value):
    dif = ((timezone.now() - value))
    if dif.days:
        dif = int(dif.days)
        unit = {'일': 31, '달': 12}
        for key, val in unit.items():
            if dif//val == 0:
                return str(dif) + key
            else:
                dif //= val
        return str(dif) + '년'

    else:
        dif = int(dif.seconds)
        unit = {'초': 60, '분': 60, '시간': 24}
        for key, val in unit.items():
            if dif//val == 0:
                return str(dif) + key
            else:
                dif //= val
