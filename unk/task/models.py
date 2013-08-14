from django.db import models
from registration.models import Customer, Supplier
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

class Currency(models.Model):
	"""Currency list"""
	name = models.CharField(max_length=20)
	code = models.CharField(max_length=3) 
	symbol = models.CharField(max_length=5)
	def __init__(self, name, code, symbol):
		super(Currency, self).__init__()
		self.name = name
		self.code = code
		self.symbol = symbol


class Service(models.Model):
	"""Service all"""
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	task_type = models.ForeignKey(TaskType)
	category = models.ForeignKey(ServiceCategory)
	value = models.IntegerField()
	currency = models.ForeignKey(Currency)
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
	def __init__(self, path, name, file_type, file_tag):
		super(Files, self).__init__()
		self.path = path
		self.name = name
		self.file_type = file_type
		self.file_tag = file_tag