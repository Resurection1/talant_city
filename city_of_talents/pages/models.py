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
    photo = models.ImageField(
        upload_to='about',
        verbose_name='photo',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'

    def __str__(self):
        return self.title
