from django.db import models

class Country(models.Model):
	"""List of countires"""
	name = models.CharField(max_length=30)
	def __init__(self, name):
		super(Country, self).__init__()
		self.name = name

class TimeZone(models.Model):
	"""List of Time zones"""
	name = models.CharField(max_length=5)
	def __init__(self, name):
		super(TimeZone, self).__init__()
		self.name = name

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
	username = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	password = models.CharField(max_length=200)
	phone = models.CharField(max_length=20)
	email = models.EmailField(max_length=75)	
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

class Customer(models.Model):
	"""Customer infos"""
	username = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	password = models.CharField(max_length=200)
	phone = models.CharField(max_length=20)
	email = models.EmailField(max_length=75)
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

class Admin(models.Model):
	"""Admin infos"""
	ADMIN_TYPE = (
		('REG', 'Regular'),
		('SUP', 'Supper'),
		)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=200)
	email = models.EmailField(max_length=75)
	a_type = models.CharField(max_length=3, choices=ADMIN_TYPE)