from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name='Админ'),
    path('pages/', include('pages.urls')),
    path('curses/', include('curses.urls')),
    path('books/', include('books.urls')),
    path('', include('site_title.urls'), name='Главная страница'),
]

if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
