from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
from django.core.context_processors import csrf
from unk.registration.models import Customer, Country, TimeZone, CustomerType
from unk.task.models import Service
import pytz
from django.contrib.auth.decorators import login_required

def service_list(request):
	services = Service.objects.all()
	context = {'services': services}
	return render(request, 'unk/service_list.html', context)

@login_required
def order_service(request):
	services = Service.objects.all()
	context = {'services': services}	
	return render(request, 'unk/service_list.html', context)

