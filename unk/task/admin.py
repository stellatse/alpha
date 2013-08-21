from django.contrib import admin
from unk.task.models import Service, Currency, TaskType, ServiceCategory, Parameter
from unk.account.models import CustomerAccount, SupplierAccount
from unk.registration.models import Customer, Supplier

class CurrencyAdmin(admin.ModelAdmin):
	fields = ['name', 'code', 'symbol']


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Service)
admin.site.register(TaskType)
admin.site.register(ServiceCategory)
admin.site.register(Parameter)
