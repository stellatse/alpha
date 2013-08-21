from django.contrib import admin
from unk.account.models import CustomerAccount, SupplierAccount
from unk.registration.models import Customer, Supplier
from unk.task.models import Service, Currency, ServiceCategory

class CurrencyAdmin(admin.ModelAdmin):
	fields = ['name', 'code', 'symbol']


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Service)
admin.site.register(ServiceCategory)
		