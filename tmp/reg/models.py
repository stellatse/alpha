from django.db import models
from django.contrib.auth.models import User
class Country(models.Model):
	"""List of countires"""
	name = models.CharField(max_length=30)
	def __unicode__(self):
        return self.name

class TimeZone(models.Model):
	"""List of Time zones"""
	name = models.CharField(max_length=5)
	def __unicode__(self):
        return self.name

class CustomerType(models.Model):
	"""List of customer types"""
	name = models.CharField(max_length=100)

class Bank(models.Model):
	"""List of bank info"""
	name = models.CharField(max_length=100)
	swift_code = models.CharField(max_length=20)
	account = models.CharField(max_length=50)
	bill_name = models.CharField(max_length=50)
	bill_address = models.TextField()

class Paypal(models.Model):
	"""List of paypal info"""
	account = models.CharField(max_length=100)
	name = models.CharField(max_length=50)

class Supplier(models.Model):
	"""Supplier info"""
	user = models.OneToOneField(User)
	phone = models.CharField(max_length=20)
	qq = models.CharField(max_length=20)
	msn = models.EmailField(max_length=75)
	ym = models.CharField(max_length=100)
	sonork = models.CharField(max_length=100)
	nation = models.ForeignKey(Country)
	address = models.CharField(max_length=200)
	timezone = models.ForeignKey(TimeZone)
	bank = models.ForeignKey(Bank)
	paypal = models.ForeignKey(Paypal)
	pin = models.CharField(max_length=4)
	locked = models.BooleanField()		

	def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)

class Customer(models.Model):
	"""Customer infos"""
	user = models.OneToOneField(User)
	phone = models.CharField(max_length=20)
	qq = models.CharField(max_length=20)
	msn = models.EmailField(max_length=75)
	ym = models.CharField(max_length=100)
	sonork = models.CharField(max_length=100)
	nation = models.ForeignKey(Country)
	address = models.CharField(max_length=200)
	timezone = models.ForeignKey(TimeZone)
	c_type = models.ForeignKey(CustomerType)
	link_supplier = models.ForeignKey(Supplier, null=True, blank=True)
	locked = models.BooleanField()
	def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.firstname, self.lastname)
    full_name = property(_get_full_name)

class Admin(models.Model):
	"""Admin infos"""
	user = models.OneToOneField(User)
	ADMIN_TYPE = (
		('REG', 'Regular'),
		('SUP', 'Supper'),
		)
	a_type = models.CharField(max_length=3, choices=ADMIN_TYPE)