# Generated by Django 3.2.16 on 2024-04-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curses', '0011_sign_up_for_a_course_customer_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign_up_for_a_course',
            name='authors_comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий клиента'),
        ),
    ]
