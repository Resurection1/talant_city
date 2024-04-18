from django.db import models

from ckeditor.fields import RichTextField

from django.core.validators import FileExtensionValidator

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
    description_comment = models.TextField(
        verbose_name='Короткое описание',
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='curse',
        verbose_name='Фотография',
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


class Reviews(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    curse = models.ForeignKey(
        Curse,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Курс'
    )

    photo = models.ImageField(
        upload_to='curse',
        verbose_name='photo',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.title[:MAX_RANGE_TITLE]


class Sign_up_for_a_course(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя')
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(max_length=256, verbose_name='Емаил')
    curse = models.ForeignKey(
        Curse,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Курсы',
    )
    customer_comment = models.TextField(
        verbose_name='Комментарий клиента',
        blank=True,
        null=True
    )

    authors_comment = models.TextField(
        verbose_name='Служебный комментарий',
        blank=True,
        null=True
    )

    call_back = models.BooleanField(
        default=True,
        verbose_name='Перезвонить',
        help_text='Клиент попросил перезвонить позже.')
    is_delete = models.BooleanField(
        default=False,
        verbose_name='Удалить',
        help_text='Клиент попросил больше не звонить.')
    is_sign_up = models.BooleanField(
        default=False,
        verbose_name='Придет на курс',
        help_text='Готов придти на курс.')

    class Meta:
        verbose_name = 'Заявки послупления на курс'
        verbose_name_plural = 'Заявки послупления на курс'

    def __str__(self):
        return self.name[:MAX_RANGE_TITLE]


class Video(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
        )
    link = models.URLField(
        verbose_name='Ссылка на видео',
        blank=True,
        null=True
    )

    video_file = models.FileField(
        verbose_name='Загрузить файл',
        upload_to='videos_curses',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv']
                )
            ]
        )

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.title[:MAX_RANGE_TITLE]
