from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView, UpdateView

from .utils import *
from .forms import *
from .models import *


class WorkersHome(DataMixin, ListView):
    model = Workers
    template_name = 'workers/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Workers page')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Workers.objects.all().select_related('cat').order_by('-id')


class AboutPage(DataMixin, TemplateView):
    template_name = 'workers/about.html'
    model = Workers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='About')

        return dict(list(context.items()) + list(c_def.items()))


class AddPage(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'workers/add_page.html'
    success_url = reverse_lazy('workers')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add worker')
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


class ShowPost(DataMixin, DetailView):
    model = Workers
    template_name = 'workers/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['posts'])
        return dict(list(context.items()) + list(c_def.items()))


class WorkersCategory(DataMixin, ListView):
    model = Workers
    template_name = 'workers/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Category - ' + str(c.name),
                                      cat_selected=c.pk)

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Workers.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')


class DeletePost(DataMixin, DeleteView):
    model = Workers
    template_name = 'workers/delete_confirm.html'
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('workers')
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['posts'])
        return dict(list(context.items()) + list(c_def.items()))


class UpdatePost(DataMixin, UpdateView):
    model = Workers
    form_class = AddPostForm
    template_name = 'workers/update_form.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Update worker')
        return dict(list(context.items()) + list(c_def.items()))
