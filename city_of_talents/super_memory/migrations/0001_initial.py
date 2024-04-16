# Generated by Django 3.2.16 on 2024-04-16 18:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curses', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Super_memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('is_published', models.BooleanField(default=True, help_text='Снимите галочку, чтобы скрыть публикацию.', verbose_name='Опубликовано')),
                ('date', models.DateTimeField(verbose_name='Дата и время конкурса')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='curse', verbose_name='photo')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='curses.location', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Конкурс супер память',
                'verbose_name_plural': 'Конкурс супер память',
            },
        ),
    ]
