from django.contrib import admin
from unk.account.models import CustomerAccount, SupplierAccount
from unk.registration.models import Customer, Supplier
from unk.task.models import Service

class CustomerAccountInline(admin.TabularInline):
	model = CustomerAccount
	extra = 3

class CustomerAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['username']})
	]
	inlines = [CustomerAccountInline]
	list_display = ('username', 'full_name')

admin.site.register(Service)

		