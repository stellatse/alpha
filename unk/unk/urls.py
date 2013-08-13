from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'unk.views.home', name='home'),
    url(r'^reg/', include(register.urls)),

    # url(r'^unk/', include('unk.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
