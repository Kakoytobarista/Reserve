# Generated by Django 3.2.4 on 2021-06-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0002_reception_reserver_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reception',
            name='date',
            field=models.DateField(verbose_name='Date of reserve'),
        ),
    ]