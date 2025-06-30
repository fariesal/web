from django.contrib import admin
from django.urls import path,  include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


from mysite.views import *
from mysite.autentication import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('artikel/<int:id>', detail_artikel, name='detail_artikel'),
    path('artikel-not-found', not_found_artikel, name='not_found_artikel'),
    path('kontak', kontak, name='kontak'),
    path('galeri', galeri, name='galeri'),
    path('about', about, name='about'),

    path('dashboard/', dashboard, name='dashboard'),

    path('dashboard/', include("artikel.urls")), 


    # autentication #
    path('auth-login', login, name='login'),
    path('auth-logout', logout, name='logout'),
    path('auth-registrasi', registrasi, name='registrasi'),
]


urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)