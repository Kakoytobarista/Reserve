from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

from .forms import *
from .models import *

menu = [
    {'title': 'About this app', 'url_name': 'about'},
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
        'title': 'О работниках',
        'menu': menu
    }
    return render(request, 'workers/about.html', context)


def add_page(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('workers')

    else:
        form = AddPostForm()

    return render(request, 'workers/add_page.html',
                  {'menu': menu,
                   'title': 'Add worker',
                   'form': form})


def contact(request):
    return HttpResponse('Feedback')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Workers, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,

    }

    return render(request, 'workers/post.html', context=context)


def show_category(request, cat_slug):
    cat = get_object_or_404(Category, slug=cat_slug)

    context = {
        'title': 'Отображение по разделам',
        'menu': menu,
        'cat_selected': cat.id,
    }

    return render(request, 'workers/index.html', context=context)
