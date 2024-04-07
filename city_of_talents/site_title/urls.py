from django.urls import path

from . import views

app_name = 'Site_title'

urlpatterns = [
    path('', views.site_title.as_view(), name='Site_title'),
]
