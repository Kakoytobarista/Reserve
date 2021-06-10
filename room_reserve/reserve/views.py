
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from django.http import HttpResponseNotFound, HttpResponse
from .forms import ReceptionForm


def index(request):
    return render(request, 'index.html')


def reserve_room(request, reserver_id):
    if request.method == 'POST':
        form = ReceptionForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('index')

    else:
        form = ReceptionForm()

    return render(request, 'reserve/reception.html',
                  {
                  'form': form})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Слушай брат, нахуй ты сюда зашел, иди на правильный редирект,'
                                '<strong>долбаеб</strong></h1>')

