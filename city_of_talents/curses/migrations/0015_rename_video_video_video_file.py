# Generated by Django 3.2.16 on 2024-04-18 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curses', '0014_alter_video_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video',
            new_name='video_file',
        ),
    ]
