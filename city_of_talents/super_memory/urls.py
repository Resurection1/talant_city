from django.urls import path

from . import views

app_name = 'super_memory'

urlpatterns = [
    path('', views.super_memory.as_view(), name='super_memory'),
]
