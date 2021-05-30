from django.shortcuts import render, HttpResponse

from .models import *


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    posts = Workers.objects.all()
    context = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts
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


def login(request):
    return HttpResponse('Log in')


def show_post(request, post_id):
    return HttpResponse(f'Hello gnida{post_id}')

