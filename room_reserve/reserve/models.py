from django.db import models
from django.shortcuts import render


class Room(models.Model):
    rooms = models.CharField(max_length=100)

    def __str__(self):
        return self.rooms


class Time(models.Model):
    time_date = models.DateTimeField('date_reserve')

    def __str__(self):
        return self.time_date


# class Login(models.Model):
#     login = models.CharField(max_length=50)
#     password = models.CharField(max_length=15)
#
#     @staticmethod
#     def get_absolute_url(request):
#         return render(request, 'reserve/reserve_update_form.html')
#
