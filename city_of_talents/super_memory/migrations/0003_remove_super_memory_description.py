# Generated by Django 3.2.16 on 2024-04-18 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_memory', '0002_auto_20240417_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super_memory',
            name='description',
        ),
    ]