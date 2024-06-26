# Generated by Django 3.2.16 on 2024-04-18 23:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curses', '0018_auto_20240419_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='videos_curses', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='Загрузить файл')),
            ],
            options={
                'verbose_name': 'Загрузить файл',
                'verbose_name_plural': 'Загрузить файл',
            },
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_file',
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.ManyToManyField(blank=True, null=True, to='curses.File_Link', verbose_name='Ссылки'),
        ),
    ]
