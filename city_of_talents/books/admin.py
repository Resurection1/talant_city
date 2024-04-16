from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'publishing_house',
        'count_of_pages',
        'format',
        'link',
        'post_photo',
        'is_published'
    )
    list_editable = (
        'is_published',
    )
    list_display_links = ('title',)

    readonly_fields = ["post_photo"]

    def post_photo(self, book):
        if book.photo:
            return mark_safe(f'<img src="{book.photo.url}" width="75" height="75">')
        return 'Нет фотографии'


admin.site.empty_value_display = 'Не задано'
