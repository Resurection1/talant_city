from django.db import models

from ckeditor.fields import RichTextField

from .constants import MAX_RANGE_TITLE
from core.models import PublishedModel
from trainer.models import Trainer


class Location(PublishedModel):
    name = models.CharField(
        max_length=256,
        verbose_name='Название места'
    )
    address = models.CharField(
        max_length=256,
        verbose_name='Адрес',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name[:MAX_RANGE_TITLE]


class Curse(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Курс'
    )

    description = RichTextField(
        verbose_name='Описание'
    )
    photo = models.ImageField(
        upload_to='curse',
        verbose_name='photo',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title[:MAX_RANGE_TITLE]


class Timetable(PublishedModel):
    curse = models.ForeignKey(
        Curse,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Курсы',
        related_name='curses'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Местоположение',
        related_name='locations'
    )
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Тренир',
        related_name='trainers'
    )
    introductory_lecture = models.DateTimeField(
        verbose_name='Дата и время первой лекции',
    )

    first_lesson = models.DateTimeField(
        verbose_name='Дата и время первого занятия'
    )

    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем — можно делать '
            'отложенные публикации.')
    )

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self):
        return self.curse.title[:MAX_RANGE_TITLE]
