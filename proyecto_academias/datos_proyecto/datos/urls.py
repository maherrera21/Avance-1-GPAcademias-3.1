from django.conf.urls import patterns, url

from portal import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'defunciones_fetales/$', views.defunciones_fetales, name='defunciones_fetales')
)