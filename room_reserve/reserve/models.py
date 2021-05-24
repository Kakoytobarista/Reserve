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


reserve_rooms = [
    {
        'name': 'Moscow',

    },
    {
        'name': 'Saint-Petersburg',
    },
    {
        'name': 'Nighniy_Novgorod'
    }]
