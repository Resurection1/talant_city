# Generated by Django 3.2.16 on 2024-04-21 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0004_alter_trainer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='surname',
            field=models.CharField(blank=True, max_length=256, verbose_name='Фамилия'),
        ),
    ]
