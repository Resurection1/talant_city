from django.db import models

from ckeditor.fields import RichTextField


class About(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок',
        help_text='Данный заголовок преднозначен для личного понимания'
    )
    text = RichTextField(
        verbose_name='О компании'
    )
    photo = models.ImageField(
        upload_to='about',
        verbose_name='photo',
        null=True,
        blank=True
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.')

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'

    def __str__(self):
        return self.title
