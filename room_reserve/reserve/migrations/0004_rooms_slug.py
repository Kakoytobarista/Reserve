# Generated by Django 3.2.4 on 2021-06-13 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0003_alter_reception_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='slug',
            field=models.SlugField(blank=True, default='DEFAULT VALUE', max_length=255, null=True, verbose_name='URL'),
        ),
    ]
