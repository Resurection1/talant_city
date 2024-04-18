# Generated by Django 3.2.16 on 2024-04-18 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curses', '0005_alter_timetable_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address_timetables', to='curses.location', verbose_name='Адрес'),
        ),
    ]
