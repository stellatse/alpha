from django.db import models
from register.models import Customer, Supplier, Admin
import os.path

FILEDIR=os.path.join(os.path.dirname(__file__), 'files').replace('\\','/')

class ReviewResult(models.Model):
	"""Review result of the task"""
	name = models.CharField(max_length=200)

class TaskType(models.Model):
	"""Task type, eg. file service/IMEI service/Server service"""
	name = models.CharField(max_length=200)

class Parameter(models.Model):
	"""Delievery time unit, eg. hours, days, weeks, months"""
	name = models.CharField(max_length=200)

class TaskStatus(models.Model):
	"""Task status"""
	name = models.CharField(max_length=200)

class ServiceCategory(models.Model):
	"""ServiceCategory, eg. Nokia,SL3(LBF)"""
	name = models.CharField(max_length=200)

class Service(models.Model):
	"""Service all""", 
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	task_type = models.ForeignKey(TaskType)
	category = models.ForeignKey(ServiceCategory)
	value = models.IntegerField()
	commit_time_from = models.IntegerField()
	commit_time_to = models.IntegerField()
	parameter = models.ForeignKey(Parameter)

class Task(models.Model):
	"""Task all"""
	name = models.CharField(max_length=200)
	status = models.ForeignKey(TaskStatus)
	task_type = models.ForeignKey(TaskType)
	service = models.ForeignKey(Service)
	imei = models.CharField(max_length=400)
	customer = models.ForeignKey(Customer)
	submit_time = models.DateTimeField(auto_now_add=True)
	supplier = models.ForeignKey(Supplier, null=True, blank=True)
	pick_time = models.DateTimeField(null=True, blank=True)
	estimate_time = models.IntegerField() # Store as int in Seconds unit
	review_time = models.DateTimeField(null=True, blank=True)
	reviewed = models.BooleanField()
	review_result = models.ForeignKey(ReviewResult)
	review_comment = models.TextField(null=True, blank=True)
	objection = models.BooleanField()
	objection_time = models.DateTimeField(null=True, blank=True)
	retracted = models.BooleanField()
	retract_reason = models.TextField(null=True, blank=True)
	comment = models.TextField(null=True, blank=True)
	final_price = models.FloatField()

class Files(models.Model):
	"""Store all the file path of tasks, including submit file and feedback file"""
	FILE_TAG_CHOICES = (
		('REQ', 'Request'),
		('RES', 'Response'),
		)
	name = models.CharField(max_length=200)
	path = models.FileField(upload_to=FILEDIR)
	file_type = models.CharField(max_length=20)
	file_tag = models.CharField(max_length=3, choices=FILE_TAG_CHOICES)
	task = models.ForeignKey(Task)

class PriceHistory(models.Model):
	"""Store all the price updated record"""
	PRICE_TYPE = (
		('INC', 'Increase'),
		('DEC', 'Decrease'),
		)
	OPERATOR_TYPE = (
		('ADM', 'Admin'),
		('CUS', 'Customer'),
		('SUP', 'Supplier'),
		)
	task = models.ForeignKey(Task)
	p_type = models.CharField(max_length=3, choices=PRICE_TYPE)
	value = models.FloatField()
	operator_type = models.CharField(max_length=3, choices=OPERATOR_TYPE)
	customer = models.ForeignKey(Customer)
	supplier = models.ForeignKey(Supplier)
	admin = models.ForeignKey(Admin)
	update_time = models.DateTimeField(auto_now=True)
	
						
