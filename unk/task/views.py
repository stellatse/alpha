from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from unk.task.models import Service, Task
from unk.task.forms import TaskForm


def service_list(request):
	services = Service.objects.all()
	print services
        context = {
		'services': services
	}
	return render(request, 'unk/services/service_list.html', context)

@login_required
def task_list(request):
	return render(request, 'unk/services/task_list.html', {
		'tasks': Task.objects.all()
	})

@login_required
def order_service(request, service_id):
	try:
		service = Service.objects.get(pk=service_id)
		if request.method == 'POST':
			pass

	except Service.DoesNotExist:
		raise Http404
	context = {'service': service, 'form': TaskForm()}
#	if request.method == 'POST':
#		print "Submit order form handle"
	return render(request, 'unk/services/service_order.html', context)

