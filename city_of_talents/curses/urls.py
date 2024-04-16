from django.urls import path

from . import views

app_name = 'curses'

urlpatterns = [
    path('<int:curs_id>/', views.curse_detail.as_view(), name='curse'),
    path('timetable/', views.timetable.as_view(), name='timetable'),
    path("", views.curse_list.as_view(), name="curses"),
]
