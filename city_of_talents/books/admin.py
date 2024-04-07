from django.contrib import admin

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
        'is_published'
    )
    list_editable = (
        'is_published',
    )
    list_display_links = ('title',)


admin.site.empty_value_display = 'Не задано'
