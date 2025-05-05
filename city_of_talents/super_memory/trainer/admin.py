from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Trainer


@admin.register(Trainer)
class TrainirAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'post_photo',
        'is_published'
    )
    list_editable = (
        'is_published',
    )

    readonly_fields = ["post_photo"]

    def post_photo(self, trainer):
        if trainer.photo:
            return mark_safe(f'<img src="{trainer.photo.url}" width="75" height="75">')
        return 'Нет фотографии'
