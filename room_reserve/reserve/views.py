from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView

from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
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

    def form_valid(self, form):
        fcd = form.cleaned_data

        response_dict = {
            "reserver_name": fcd['reserver_name'],
            'form': form,
            "curr_date": fcd['date'],
            "curr_time": fcd['time_since'],
            "until_time": fcd['time_until'],
            "curr_reserver": fcd['reserver']
        }

        current_session = {'time_since': fcd['time_since'],
                           'time_until': fcd['time_until']}

        current_booking_day = Reception.objects.filter(date=fcd['date'],
                                                       reserver=fcd['reserver']).values('time_since',
                                                                                        'time_until')

        for i in current_booking_day:
            if i['time_since'] <= current_session['time_until'] and current_session['time_since'] <= i['time_until']:
                response_dict["message"] = "This registration date is already taken, please choose another date."
                return render(self.request, 'reserve/reception.html', response_dict)

        else:
            Reception.objects.create(date=fcd['date'], time_since=fcd['time_since'],
                                     time_until=fcd['time_until'],
                                     reserver_name=fcd['reserver_name'],
                                     reception_info=fcd['reception_info'],
                                     reserver=fcd['reserver'])

            return render(self.request, 'reserve/reception.html', response_dict)

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


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'reserve/contact.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        print(form.cleaned_data)
        fcd = form.cleaned_data
        uploaded_file = fcd['photo']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        return redirect('index')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Wrong url')


def feedback(request):
    return HttpResponse('Hello')

