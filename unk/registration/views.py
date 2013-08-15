from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json

def home(request):
    return render(request, 'account/index.html')

# json request ?
def login(request):
    ret = []
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username, password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            print("User is valid, active and authenticated")
        else:
            print("The password is valid, but the account has been disabled!")
    else:
        # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
    context = {}
    return render(request, 'index.html', context)

def register(request):
    username = request.POST['username']


def logout(request):
    return render(request, '')
