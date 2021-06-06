from django import template
from ..models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('workers/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {
        "cats": cats,
        "cat_selected": cat_selected,
    }


@register.simple_tag()
def get_posts(cat_id=None):
    if not cat_id:
        return Workers.objects.all()

    else:
        return Workers.objects.filter(cat_id=cat_id)


@register.inclusion_tag('workers/list_posts.html')
def show_posts(sort=None):
    if not sort:
        posts = Workers.objects.all()
    else:
        posts = Workers.objects.order_by(sort)

    return {
        "posts": posts,

    }
