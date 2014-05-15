from django.conf.urls import patterns, url

from top14 import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index')
)
