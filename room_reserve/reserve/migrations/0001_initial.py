# Generated by Django 3.2 on 2021-06-03 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Room')),
                ('info', models.CharField(max_length=300, verbose_name='Info about room')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date of reserve')),
                ('time', models.CharField(max_length=5, verbose_name='Time')),
                ('reception_info', models.CharField(max_length=1000, verbose_name='Info about reserver')),
                ('reserver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reserve.rooms', verbose_name='Reserver ')),
            ],
        ),
    ]
