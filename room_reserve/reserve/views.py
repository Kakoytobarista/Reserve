from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import ReceptionForm
from .models import *
from django.http import HttpResponseNotFound, HttpResponse
from .forms import ReceptionForm


def index(request):
    return render(request, 'index.html')


class ReceptionView(FormView):
    form_class = ReceptionForm
    template_name = 'reserve/reception.html'

    def reserve_room(self, request):
        form = self.form_class()
        selected_date = ''
        selected_time = ''
        selected_info = ''

        if request.method == 'POST':
            selected_date = request.POST['date_of_reserve']
            selected_time = request.POST['time']
            selected_info = request.POST['info_about_reserve']

        context = {
            'selected_date': selected_date,
            'selected_time': selected_time,
            'selected_info': selected_info,
            'form': form
        }
        print(context)
        return render(request, self.template_name, context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Слушай брат, нахуй ты сюда зашел, иди на правильный редирект,'
                                '<strong>долбаеб</strong></h1>')


    # def form_valid(self, form):
    #     fcd = form.cleaned_data
    #     current_room = Rooms.objects.get(id=self.kwargs['room_id'])
    #     response_dict = {
    #                     "form": form,
    #                     "doctor": current_room,
    #                     "curr_date": fcd['date'],
    #                     "curr_time": fcd['time']}
    #     # условие для предотвращения записи на один и тот же деь у данного врача
    #     if Reception.objects.filter(date=fcd['date'], time=fcd['time'], rooms=current_room).count() == 0:
    #         Reception.objects.create(date=fcd['date'], time=fcd['time'],
    #                                  patient_name=fcd['reception_info'],
    #                                  patient_info=fcd['reception_info'],
    #                                  rooms=current_room)
    #         return render('reception.html', response_dict, RequestContext(self.request))
    #     else:
    #         response_dict["message"] = "Вы уже зарегистрированны на это время"
    #         return render('reserve/reception.html', response_dict, RequestContext(self.request))