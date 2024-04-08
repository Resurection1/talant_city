from django.contrib import admin

from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    list_display_links = ('title',)


admin.site.empty_value_display = 'Не задано'
