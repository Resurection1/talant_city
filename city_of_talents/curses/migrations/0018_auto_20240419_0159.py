# Generated by Django 3.2.16 on 2024-04-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curses', '0017_auto_20240419_0151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'Ссылка на видео', 'verbose_name_plural': 'Ссылка на видео'},
        ),
        migrations.RemoveField(
            model_name='video',
            name='link',
        ),
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.ManyToManyField(blank=True, null=True, to='curses.Link', verbose_name='Ссылки'),
        ),
    ]
