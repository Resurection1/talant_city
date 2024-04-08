from django.db import models

from ckeditor.fields import RichTextField


class About(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок'
    )
    text = RichTextField(
        verbose_name='О компании'
    )

    class Meta:
        verbose_name = 'компании'
        verbose_name_plural = 'О компании'

    def __str__(self):
        return self.title
