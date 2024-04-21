from django.contrib import admin
from .models import Super_memory
from django.utils.safestring import mark_safe


@admin.register(Super_memory)
class TrainirAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'location',
        'date',
        'post_photo',
        'is_published',
    )
    list_filter = ('title', 'date')
    list_editable = (
        'is_published',
    )

    readonly_fields = ["post_photo"]
    filter_horizontal = ('link', )

    def post_photo(self, memory):
        if memory.photo:
            return mark_safe(f'<img src="{memory.photo.url}" width="75" height="75">')
        return 'Нет фотографии'


admin.site.empty_value_display = 'Не задано'
