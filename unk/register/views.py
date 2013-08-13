from django.shortcuts import render

def home(request):
    return render(request, 'register/index.html')

# json request ?
def login(request):
    context = {}
    return render(request, 'register/login.html', context)