from unk.registration.models import Country
from unk.registration.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from pytz import all_timezones

def home(request):
    countries = Country.objects.all()
    form = RegistrationForm({
        'timezone': 'UTC',
        'nation': 'China'
    })
    timezones = all_timezones
    return render(request, 'unk/index.html', {
        'countries':countries, 
        'timezones': timezones
    })

def logout_view(request):
    logout(request)
    return redirect('home')
