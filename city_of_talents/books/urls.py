from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('<int:books_id>/', views.books_detail.as_view(), name='books'),
    path('', views.books_list.as_view(), name='books'),
]
