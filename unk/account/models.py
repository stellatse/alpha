from django.db import models
from unk.registration.models import Customer, Supplier, Admin
import os.path


class CustomerAccount(models.Model):
	"""Customer account info records"""
	ACCOUNT_TYPE = (
		('INC', 'Increase'),
		('DEC', 'Decrease'),
		('NUL', 'Nothing'),
		)
	customer = models.ForeignKey(Customer)
	a_type = models.CharField(max_length=3, choices=ACCOUNT_TYPE)
	number = models.IntegerField()
	result = models.IntegerField()
	operator = models.ForeignKey(Admin)
	udpate_time = models.DateTimeField(auto_now=True)


class SupplierAccount(models.Model):
	"""Supplier account info records"""
	ACCOUNT_TYPE = (
		('INC', 'Increase'),
		('DEC', 'Decrease'),
		('NUL', 'Nothing'),
		)
	supplier = models.ForeignKey(Supplier)
	a_type = models.CharField(max_length=3, choices=ACCOUNT_TYPE)
	number = models.IntegerField()
	result = models.IntegerField()
	operator = models.ForeignKey(Admin)
	udpate_time = models.DateTimeField(auto_now=True)