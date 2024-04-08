from django.contrib import admin
from .models import Trainer, Curse, Location


@admin.register(Trainer)
class TrainirAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'is_published',
    )
    list_editable = (
        'is_published',
    )

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
        'location',
        'introductory_lecture',
        'first_lesson',
        'pub_date',
        'is_published'
    )
    list_editable = (
        'is_published',
    )
    list_display_links = ('title',)


admin.site.empty_value_display = 'Не задано'
