from django.shortcuts import render

def home(request):
    return render(request, 'unk/index.html')