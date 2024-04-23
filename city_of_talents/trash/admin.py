from django.contrib import admin

from .models import Trash_File_Link


@admin.register(Trash_File_Link)
class AdminTrashLink(admin.ModelAdmin):
    list_display = (
        'title',
        'file'
    )
    list_display_links = ('title',)
