from django.db import models

from curses.constants import MAX_RANGE_TITLE


class Trash_File_Link(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Заголовок',
    )
    file = models.FileField(
        verbose_name='Загрузить файл',
        upload_to='all_file',
        help_text=('Выберите текстовый файл для загрузки на сервер'
                   'и дальнейшего использования в тексовом редакторе'),
    )

    class Meta:
        verbose_name = 'Загрузить файл'
        verbose_name_plural = 'Загрузить файлы'

    def __str__(self):
        return self.title[:MAX_RANGE_TITLE]
