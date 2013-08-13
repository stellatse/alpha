from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def home(request):
    return render(request, 'account/index.html')

# json request ?
def login(request):
    username = 'admin'
    password = 'admin'
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

def logout(request):
    return render(request, '')
