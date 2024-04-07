from django.contrib import admin

from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


admin.site.empty_value_display = 'Не задано'
