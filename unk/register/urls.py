from django.conf.urls import patterns, url

from unk.register import views

urlpatterns = patterns('',
	url(r'^login/', views.login, name='login'),

	)

