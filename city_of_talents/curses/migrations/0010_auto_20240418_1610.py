# Generated by Django 3.2.16 on 2024-04-18 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curses', '0009_auto_20240418_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_up_for_a_course',
            name='curse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='curses.curse', verbose_name='Курсы'),
        ),
        migrations.AlterField(
            model_name='sign_up_for_a_course',
            name='is_delete',
            field=models.BooleanField(default=False, help_text='Клиент попросил больше не звонить.', verbose_name='Удалить'),
        ),
        migrations.AlterField(
            model_name='sign_up_for_a_course',
            name='is_sign_up',
            field=models.BooleanField(default=False, help_text='Готов придти на курс.', verbose_name='Придет на курс'),
        ),
    ]
