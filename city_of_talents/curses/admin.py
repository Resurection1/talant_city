from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Curse, Location, Timetable, Reviews


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
    )
    list_display_links = ('name',)


@admin.register(Curse)
class AdminCurse(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'post_photo',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    list_display_links = ('title',)

    readonly_fields = ["post_photo"]

    def post_photo(self, curse):
        if curse.photo:
            return mark_safe(f'<img src="{curse.photo.url}" width="75" height="75">')
        return 'Нет фотографии'


@admin.register(Timetable)
class AdminTimetable(admin.ModelAdmin):
    list_display = (
        'curse',
        'location',
        'trainer',
        'introductory_lecture',
        'first_lesson',
        'pub_date',
        'is_published'
    )
    list_editable = (
        'is_published',
    )
    list_display_links = ('curse',)


@admin.register(Reviews)
class AdminReviews(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'curse',
        'post_photo',
        'is_published'

    )
    list_editable = (
        'is_published',
    )

    list_display_links = ('title',)

    readonly_fields = ["post_photo"]

    def post_photo(self, reviews):
        if reviews.photo:
            return mark_safe(f'<img src="{reviews.photo.url}" width="75" height="75">')
        return 'Нет фотографии'


admin.site.empty_value_display = 'Не задано'
