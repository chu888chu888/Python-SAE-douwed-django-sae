from django.conf.urls import patterns, include, url
from django.contrib import admin
from douwed.views import *
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'', include('social_auth.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^reg/$', reg),
                       url(r'^logout/$', logout),
                       url(r'^$', index),
                       url(r'^about/$', about),
                       )
