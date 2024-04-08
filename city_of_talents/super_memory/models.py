from django.db import models
from ckeditor.fields import RichTextField


class Super_memory(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок'
    )
    description = RichTextField(
        verbose_name='Описание'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.')

    class Meta:
        verbose_name = 'Конкурс супер память'
        verbose_name_plural = 'Конкурс супер память'

    def __str__(self):
        return self.title
