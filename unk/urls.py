from django.conf.urls import patterns, include, url
from django.contrib import admin
import unk.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', unk.views.home, name='home'),
    url(r'^registration/', include('unk.registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^s/', include('unk.task.urls'))
)
