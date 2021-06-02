from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, HttpResponse

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def index(request):
    posts = Workers.objects.all()
    cats = Category.objects.all()

    context = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cats': cats,
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
    posts = Workers.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'title': 'Отображение по разделам',
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'cat_selected': cat_id,
    }

    return render(request, 'workers/index.html', context=context)
