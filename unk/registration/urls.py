from django.conf.urls import patterns, url

from unk.registration import views

urlpatterns = patterns('',
	url(r'^login/', 'django.contrib.auth.views.login', name='login'),
	url(r'^reg/', 'unk.registration.views.register', name='register')
	)

