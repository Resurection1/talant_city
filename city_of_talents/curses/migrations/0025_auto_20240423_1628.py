# Generated by Django 3.2.16 on 2024-04-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curses', '0024_auto_20240421_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curse',
            name='link',
            field=models.ManyToManyField(blank=True, help_text='Видео загружается ссылкой с Ютуба', to='curses.Link', verbose_name='Ссылки'),
        ),
        migrations.AlterField(
            model_name='curse',
            name='photo',
            field=models.ImageField(blank=True, help_text='Форматы изображения jpg и png', null=True, upload_to='curse', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(blank=True, help_text='Видео загружается ссылкой с Ютуба', null=True, verbose_name='Ссылка на видео'),
        ),
    ]
