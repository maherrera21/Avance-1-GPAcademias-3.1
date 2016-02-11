
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^index','datos_proyecto.views.index', name='index'),
    url(r'^listar','datos_proyecto.views.listar', name='listar'),
    url(r'^datos','datos_proyecto.views.datos', name='datos'),
)

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)