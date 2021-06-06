from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, HttpResponse

from .models import *

menu = [{'title': 'About this app', 'url_name': 'about'},
        {'title': 'Add worker', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'Back to page reserve', 'url_name': 'index'},
        ]


def index(request):

    context = {
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': 0,
    }

    return render(request, 'workers/index.html', context=context)


def about(request):
    context = {
        'title': 'О работниках'
    }
    return render(request, 'workers/about.html', context)


def addpage(request):
    return HttpResponse('Add article')


def contact(request):
    return HttpResponse('Feedback')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_post(request, post_id):
    return HttpResponse(f'Hello gnida{post_id}')


def show_category(request, cat_id):

    context = {
        'title': 'Отображение по разделам',
        'menu': menu,
        'cat_selected': cat_id,
    }

    return render(request, 'workers/index.html', context=context)
