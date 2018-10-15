# coding: utf-8

from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

import example.views as views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.get_post, name='get_post'),
    path('about/', views.AboutView.as_view(), name='about'),

    path('stats/', include('statsy.urls')),
    path('tests/', include('tests.urls')),

    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns.append(
            path('__debug__/', include(debug_toolbar.urls)),
        )
    except ImportError:
        pass
