from django.forms import ModelForm
from unk.task.models import Task

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['imei']