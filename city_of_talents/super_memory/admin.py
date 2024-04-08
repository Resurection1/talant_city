from django.contrib import admin
from .models import Super_memory


@admin.register(Super_memory)
class TrainirAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
