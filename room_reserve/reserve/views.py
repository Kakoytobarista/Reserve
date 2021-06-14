from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView

from django.http import HttpResponseNotFound, HttpResponse
from .models import Rooms
from .forms import *
from .utils import *


class MainPage(LoginRequiredMixin, DataMixin, ListView):
    model = Rooms
    template_name = 'index.html'
    context_object_name = 'rooms'
    login_url = 'accounts/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main page')

        return dict(list(context.items()) + list(c_def.items()))


class AddReserve(LoginRequiredMixin, CreateView):
    form_class = ReceptionForm
    template_name = 'reserve/reception.html'
    context_object_name = 'form'
    extra_context = {
        'title': 'Reserve room'
    }
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class DetailRoom(LoginRequiredMixin, DataMixin, DetailView):
    model = Rooms
    template_name = 'reserve/detail_room.html'
    slug_url_kwarg = 'reserver_slug'
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['room'])
        return dict(list(context.items()) + list(c_def.items()))


def reserve_room(request, reserver_id):
    reserve_room = get_object_or_404(Rooms, id=reserver_id)
    if request.method == 'POST':
        form = ReceptionForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('index')

    else:
        form = ReceptionForm()

    return render(request, 'reserve/reception.html',
                  {
                  'form': form,
                  'room_selected': reserve_room.name,
                  })


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Слушай брат, нахуй ты сюда зашел, иди на правильный редирект,'
                                '<strong>долбаеб</strong></h1>')
