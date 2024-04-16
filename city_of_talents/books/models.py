from django.db import models

from core.models import PublishedModel


class Book(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    author = models.CharField(
        max_length=256,
        verbose_name='Автор публикации',
        null=True,
        blank=True
    )
    publishing_house = models.CharField(
        max_length=256,
        verbose_name='Издательство',
        null=True,
        blank=True
    )
    the_year_of_publishing = models.CharField(
        max_length=256,
        verbose_name='год издания',
        null=True
    )
    ISBN = models.CharField(
        max_length=256,
        verbose_name='ISBN',
        null=True,
        blank=True
    )
    count_of_pages = models.IntegerField(
        verbose_name='Число страниц'
    )
    format = models.CharField(
        max_length=256,
        verbose_name='Формат'
    )
    circulation = models.CharField(
        max_length=256,
        verbose_name='Тираж'
    )
    link = models.URLField(
        verbose_name='Ссылка на скачивание',
        null=True,
        blank=True,
        help_text='Введите ссылку на скачивание'
    )
    photo = models.ImageField(
        upload_to='book',
        verbose_name='photo',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'Книги'
