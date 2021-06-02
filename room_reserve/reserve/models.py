from django.db import models
from django.urls import reverse


class Rooms(models.Model):
    name = models.CharField(verbose_name='Room', max_length=300)
    info = models.CharField(verbose_name='Info about room', max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('room', kwargs={'room_id': self.pk})


class Reception(models.Model):
    date = models.DateTimeField(verbose_name='Date of reserve')
    time = models.CharField(verbose_name='Time', max_length=5)
    reserver = models.CharField(verbose_name='Reserver', max_length=300)

    def __str__(self):
        return 'Прием № %s' % self.id


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
