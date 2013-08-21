from unk.registration.models import Country
from unk.registration.forms import RegistrationForm
from django.shortcuts import render
#import pytz

def home(request):
    countries = Country.objects.all()
    form = RegistrationForm({
        'timezone': 'UTC'
    })
    return render(request, 'unk/index.html', {
        'countries':countries, 
        'form': form
    })
