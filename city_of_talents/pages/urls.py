from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about.as_view(), name='about'),
    path('timetable/', views.timetable.as_view(), name='timetable')

]
