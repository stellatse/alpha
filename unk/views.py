from unk.registration.models import Country
from django.shortcuts import render
import pytz
def home(request):
    countries = Country.objects.all()
    context = {'countries':countries, 'timezones': pytz.common_timezones}
    return render(request, 'unk/index.html', context)
