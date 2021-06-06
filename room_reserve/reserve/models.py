from django.db import models
from django.urls import reverse


class Rooms(models.Model):
    name = models.CharField(verbose_name='Room', max_length=300)
    info = models.CharField(verbose_name='Info about room', max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reception', kwargs={'reserver_id': self.pk})

    class Meta:
        verbose_name_plural = "Rooms"
        verbose_name = "Room"


class Reception(models.Model):
    date = models.DateTimeField(verbose_name='Date of reserve')
    time = models.CharField(verbose_name='Time', max_length=5)
    reserver_name = models.CharField(verbose_name='Full name', max_length=200)
    reception_info = models.CharField(verbose_name='Info about reserver', max_length=1000)
    reserver = models.ForeignKey(Rooms, verbose_name='Reserver ', on_delete=models.PROTECT)

    def __str__(self):
        return 'Прием № %s' % self.id

