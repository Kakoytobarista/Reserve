# Generated by Django 3.2.4 on 2021-06-27 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0006_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workers',
            name='is_published',
        ),
    ]
