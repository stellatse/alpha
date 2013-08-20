from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
from django.core.context_processors import csrf
from unk.registration.models import Customer, Country, TimeZone, CustomerType
import pytz

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
    return render(request, 'unk/index.html', context)

def register(request):
    ret = {}
    ret.update(csrf(request))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        if password != password2:
            ret.append({'status': 'Fail', 'msg': 'password not consistent'})
            return ret
        email = request.POST['email']
        phone = request.POST['phone']
        nation = request.POST['nation']
        country = Country.objects.filter(iso_3166_1_numeric=int(nation))
        timezone = pytz.timezone(request.POST['timezone'])
        request.session['django_timezone'] = timezone
        address = request.POST['address']
        user = User.objects.create_user(username, email, password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        tz = TimeZone(name=timezone)
        tz.save()
        customer_type = CustomerType.objects.get(pk=1)
        customer = Customer(user=user, phone=phone, nation=country, address=address, timezone=tz, c_type=customer_type)

    return render(request, 'unk/index.html', ret)


def logout(request):
    return render(request, '')
