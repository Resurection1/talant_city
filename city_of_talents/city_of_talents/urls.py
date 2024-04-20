from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='Админ'),
    path('curses/', include('curses.urls')),
    path('books/', include('books.urls')),
    path('super_memory/', include('super_memory.urls')),
    path('trainer/', include('trainer.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path('', include('site_title.urls'), name='Главная страница'),
if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
