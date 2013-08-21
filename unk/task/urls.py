from django.conf.urls import patterns, url

from unk.task import views

urlpatterns = patterns('',
	url(r'^list/', 'unk.task.views.service_list', name='service_list')
	)

