# Generated by Django 3.2.4 on 2021-06-22 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-name'], 'verbose_name': 'Position of work', 'verbose_name_plural': 'Positions of work'},
        ),
    ]
