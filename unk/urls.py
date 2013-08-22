from django.conf.urls import patterns, include, url
from django.contrib import admin
from unk import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', unk.views.home, name='home'),
    url(r'^registration/', include('unk.registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^s/', include('unk.task.urls')),
    url(r'^logout', views.logout, name='logout')
)
