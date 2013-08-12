from django.db import models

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


		