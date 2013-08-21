from django.contrib import admin
from unk.task.models import Service, Currency, TaskType, ServiceCategory, Parameter

admin.site.register(Currency)
admin.site.register(Service)
admin.site.register(TaskType)
admin.site.register(ServiceCategory)
admin.site.register(Parameter)
