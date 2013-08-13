from django.conf.urls import patterns, include, url
from django.contrib import admin
from unk.register import views
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'unk.views.home', name='home'),
    url(r'^$', views.home, name='home'),
    url(r'^register/', include('unk.register.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
