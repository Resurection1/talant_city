# Generated by Django 3.2.16 on 2024-04-18 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curses', '0006_alter_timetable_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='address',
        ),
    ]
