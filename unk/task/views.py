from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from unk.task.models import Service

def service_list(request):
	services = Service.objects.all()
	context = {
		'services': services
	}
	return render(request, 'unk/services/service_list.html', context)

@login_required
def order_service(request):
	services = Service.objects.all()
	context = {'services': services}	
	return render(request, 'unk/services/service_list.html', context)

