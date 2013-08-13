from django.conf.urls import patterns, url

from unk.account import views

urlpatterns = patterns('',
	url(r'^login/', 'django.contrib.auth.views.login', name='login'),
	)

