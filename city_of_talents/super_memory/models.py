from django.db import models
from ckeditor.fields import RichTextField

from curses.models import Location


class Super_memory(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.')
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Место'
    )
    date = models.DateTimeField(
        verbose_name='Дата и время конкурса',
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='super_memory',
        verbose_name='photo',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Конкурс супер память'
        verbose_name_plural = 'Конкурс супер память'

    def __str__(self):
        return self.title
