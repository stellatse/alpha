from django.conf.urls import patterns, url

from unk.registration import views

urlpatterns = patterns('',
	url(r'^login/', 'unk.registration.views.login', name='login'),
	url(r'^reg/', 'unk.registration.views.register', name='register')
	)

