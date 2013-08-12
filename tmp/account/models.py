from django.db import models
from register.models import Customer, Supplier, Admin
import os.path


class CustomerAccount(models.Model):
	"""Customer account info records"""
	customer = models.ForeignKey(Customer)
	