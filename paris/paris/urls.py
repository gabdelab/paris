from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'paris.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^top14/', include('top14.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
