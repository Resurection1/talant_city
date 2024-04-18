from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'post_photo',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    list_display_links = ('title',)

    readonly_fields = ["post_photo"]

    def post_photo(self, about):
        if about.photo:
            return mark_safe(f'<img src="{about.photo.url}" width="75" height="75">')
        return 'Нет фотографии'


admin.site.empty_value_display = 'Не задано'
