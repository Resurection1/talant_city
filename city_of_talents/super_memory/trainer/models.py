from django.db import models

from ckeditor.fields import RichTextField

from .constants import MAX_RANGE_TITLE


class Trainer(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Имя'
    )
    surname = models.CharField(
        max_length=256,
        verbose_name='Фамилия',
        blank=True
    )
    description = RichTextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.')
    photo = models.ImageField(
        upload_to='trainers',
        help_text='Форматы изображения jpg и png'
        )

    class Meta:
        verbose_name = 'тренeра'
        verbose_name_plural = 'Тренeры'

    def __str__(self):
        return self.name[:MAX_RANGE_TITLE]
