from django import forms
from timezone_field import TimeZoneFormField
#from django_countries import CountryField

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)
    timezone = TimeZoneFormField()
#    nation = CountryField()
    firstname = forms.CharField(max_length=100, required=False)
    lastname = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    address = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=100, required=False)


    
    