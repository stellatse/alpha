from django.contrib import admin
from unk.account.models import CustomerAccount, SupplierAccount
from unk.registration.models import Customer, Supplier
from unk.task.models import Service, Currency

admin.site.register(Currency)
admin.site.register(Service)

		