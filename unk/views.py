from unk.registration.models import Country
from django.shortcuts import render

def home(request):
    countries = Country.objects.all()
    context = {'countries':countries}
    return render(request, 'unk/index.html', context)
