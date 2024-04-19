from django.utils.html import format_html

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Curse, Location, Timetable,
                     Reviews, Sign_up_for_a_course, Video, Link)


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
            return mark_safe(
                f'<img src="{curse.photo.url}" width="75" height="75">'
            )
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
            return mark_safe(
                f'<img src="{reviews.photo.url}" width="75" height="75">'
            )
        return 'Нет фотографии'


@admin.register(Sign_up_for_a_course)
class AdminSign_up_for_a_course(admin.ModelAdmin):
    list_display = (
        'name',
        'phone_number',
        'email',
        'curse',
        'customer_comment',
        'authors_comment',
        'is_sign_up',
        'call_back',
        'is_delete'
    )
    list_editable = (
        'authors_comment',
        'is_sign_up',
        'call_back',
        'is_delete'
    )

    list_display_links = ('name',)
    list_filter = ('name', 'is_sign_up', 'call_back')


@admin.register(Video)
class AdminVideo(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published'
    )
    list_display_links = ('title',)

    list_editable = (
        'description',
        'is_published'
    )

    list_filter = ('title', 'is_published')
    filter_horizontal = ('link',)


@admin.register(Link)
class AdminVideoLink(admin.ModelAdmin):
    list_display = ('title', 'url')


# @admin.register(File_Link)
# class AdminVideoFileLink(admin.ModelAdmin):
#     list_display = ('title', 'play_video')

#     def play_video(self, obj):
#         return format_html('<a href="{}" target="_blank">{}</a>',
#                            obj.video_file.url, obj.video_file.name)
    


admin.site.empty_value_display = 'Не задано'
