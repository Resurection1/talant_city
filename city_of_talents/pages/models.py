from django.db import models


class About(models.Model):
    text = models.TextField(
        verbose_name='О компании'
    )

    class Meta:
        verbose_name = 'компании'
        verbose_name_plural = 'О компании'

    def __str__(self):
        return self.text
