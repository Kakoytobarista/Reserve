# Generated by Django 3.2 on 2021-06-05 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reception',
            name='reserver_name',
            field=models.CharField(default=datetime.date(2021, 6, 5), max_length=200, verbose_name='Full name'),
            preserve_default=False,
        ),
    ]
