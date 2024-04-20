from django.urls import path

from . import views

app_name = 'curses'

urlpatterns = [
    path('<int:curs_id>/', views.curse_detail.as_view(), name='curse'),
    path('timetable/', views.timetable.as_view(), name='timetable'),
    path('sign-up-for-a-course/', views.sign_up_for_a_course.as_view(),
         name='sign-up-for-a-course'),
    path('reviews/', views.reviews.as_view(), name='reviews'),
    path('video/', views.video_list.as_view(), name='video'),
    path("", views.curse_list.as_view(), name="curses"),
]
