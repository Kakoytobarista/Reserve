from django.db import models
from django.urls import reverse


class Rooms(models.Model):
    name = models.CharField(verbose_name='Room', max_length=300)
    info = models.CharField(verbose_name='Info about room', max_length=300)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL", default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={
            'reserver_slug': self.slug})

    class Meta:
        verbose_name_plural = "Rooms"
        verbose_name = "Room"


class Reception(models.Model):
    date = models.DateField(verbose_name='Date of reserve')
    time_since = models.CharField(verbose_name='Time since', max_length=10, null=True)
    time_until = models.CharField(verbose_name='Time until', max_length=10, null=True)
    reserver_name = models.CharField(verbose_name='Full name', max_length=200)
    reception_info = models.CharField(verbose_name='Info about reserver', max_length=1000)
    reserver = models.ForeignKey(Rooms, verbose_name='Reserver ', on_delete=models.PROTECT)

    def __str__(self):
        return 'Резерв № %s' % self.id
