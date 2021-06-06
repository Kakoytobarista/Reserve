from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import ReceptionForm
from django.http import JsonResponse
from django.template import RequestContext
from .models import *
from django.http import HttpResponseNotFound, HttpResponse


def index(request):
    return render(request, 'index.html')


def show_room(request, room_id):
    return HttpResponse(f'Hello gnida{room_id}')


class ReceptionView(FormView):
    form_class = ReceptionForm
    template_name = 'reserve/reception.html'

    def form_valid(self, form):
        fcd = form.cleaned_data
        current_room = Rooms.objects.get(id=self.kwargs['room_id'])
        response_dict = {
                        "form": form,
                        "doctor": current_room,
                        "curr_date": fcd['date'],
                        "curr_time": fcd['time']}
        # условие для предотвращения записи на один и тот же деь у данного врача
        if Reception.objects.filter(date=fcd['date'], time=fcd['time'], rooms=current_room).count() == 0:
            Reception.objects.create(date=fcd['date'], time=fcd['time'],
                                     patient_name=fcd['reception_info'],
                                     patient_info=fcd['reception_info'],
                                     rooms=current_room)
            return render('reception.html', response_dict, RequestContext(self.request))
        else:
            response_dict["message"] = "Вы уже зарегистрированны на это время"
            return render('reserve/reception.html', response_dict, RequestContext(self.request))

    def get_context_data(self, **kwargs):
        context = super(ReceptionView, self).get_context_data(**kwargs)
        context['rooms'] = Rooms.objects.get(id=self.kwargs['reserver_id'])
        return context


def date_from_ajax(request):
    if request.method == "POST" and request.is_ajax():
        room = Rooms.objects.get(id=request.POST.get("rooms_id"))
        reception_set = room.reception_set.filter(date=request.POST.get("date_from_ajax"))
        time_list = []
        for reception in reception_set:
            time_list.append(reception.time)
        return JsonResponse({'time_list': time_list})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Слушай брат, нахуй ты сюда зашел, иди на правильный редирект,'
                                '<strong>долбаеб</strong></h1>')
