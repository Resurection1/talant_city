# Generated by Django 3.2.16 on 2024-04-22 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_memory', '0005_super_memory_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super_memory',
            name='link',
        ),
    ]
