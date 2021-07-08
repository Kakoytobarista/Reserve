from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def get_rooms():
    return Rooms.objects.all()


@register.simple_tag()
def get_all_reserve():
    return Reception.objects.order_by('date')


@register.simple_tag()
def get_moscow_reserve():
    return Reception.objects.filter(reserver=1)


@register.simple_tag()
def get_saintp_reserve():
    return Reception.objects.filter(reserver=2)


@register.simple_tag()
def get_samara():
    return Reception.objects.filter(reserver=3)
