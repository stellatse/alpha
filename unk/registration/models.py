from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
class Country(models.Model):
    """
    International Organization for Standardization (ISO) 3166-1 Country list.
    """
    iso_3166_1_a2 = models.CharField(_('ISO 3166-1 alpha-2'), max_length=2,
                                     primary_key=True)
    iso_3166_1_a3 = models.CharField(_('ISO 3166-1 alpha-3'), max_length=3,
                                     null=True, db_index=True)
    iso_3166_1_numeric = models.PositiveSmallIntegerField(
        _('ISO 3166-1 numeric'), null=True, db_index=True)
    name = models.CharField(_('Official name (CAPS)'), max_length=128)
    printable_name = models.CharField(_('Country name'), max_length=128)

    display_order = models.PositiveSmallIntegerField(
        _("Display order"), default=0, db_index=True,
        help_text=_('Higher the number, higher the country in the list.'))

    is_shipping_country = models.BooleanField(_("Is Shipping Country"),
                                              default=False, db_index=True)

    def __unicode__(self):
        return self.printable_name or self.name

class TimeZone(models.Model):
	"""List of Time zones"""
	name = models.CharField(max_length=5)

	def __unicode__(self):
		return self.name

class CustomerType(models.Model):
	"""List of customer types"""
	name = models.CharField(max_length=100)

class Bank(models.Model):
	"""List of bank info"""
	name = models.CharField(max_length=100)
	swift_code = models.CharField(max_length=20)
	account = models.CharField(max_length=50)
	bill_name = models.CharField(max_length=50)
	bill_address = models.TextField()

class Paypal(models.Model):
	"""List of paypal info"""
	account = models.CharField(max_length=100)
	name = models.CharField(max_length=50)

class Supplier(models.Model):
	"""Supplier info"""
	user = models.OneToOneField(User)
	phone = models.CharField(max_length=20)
	qq = models.CharField(max_length=20)
	msn = models.EmailField(max_length=75)
	ym = models.CharField(max_length=100)
	sonork = models.CharField(max_length=100)
	nation = models.ForeignKey(Country)
	address = models.CharField(max_length=200)
	timezone = models.ForeignKey(TimeZone)
	bank = models.ForeignKey(Bank)
	paypal = models.ForeignKey(Paypal)
	pin = models.CharField(max_length=4)
	locked = models.BooleanField()		

	def _get_full_name(self):
		return '%s %s' % (self.first_name, self.last_name)
	
	full_name = property(_get_full_name)

class Customer(models.Model):
	"""Customer infos"""
	user = models.OneToOneField(User)
	phone = models.CharField(max_length=20)
	qq = models.CharField(max_length=20)
	msn = models.EmailField(max_length=75)
	ym = models.CharField(max_length=100)
	sonork = models.CharField(max_length=100)
	nation = models.ForeignKey(Country)
	address = models.CharField(max_length=200)
	timezone = models.ForeignKey(TimeZone)
	c_type = models.ForeignKey(CustomerType)
	link_supplier = models.ForeignKey(Supplier, null=True, blank=True)
	locked = models.BooleanField(default=False)
	def _get_full_name(self):
		return '%s %s' % (self.first_name, self.last_name)
	full_name = property(_get_full_name)

	class Admin:
		list_display = ('user', 'full_name', 'phone', 'qq', 'msn', 'ym', 'sonork', 'nation', 'address', 'timezone', 'c_type', 'link_supplier', 'locked' )
			

class Administrator(models.Model):
	"""Admin infos"""
	user = models.OneToOneField(User)
	ADMIN_TYPE = (
		('REG', 'Regular'),
		('SUP', 'Supper'),
		)
	a_type = models.CharField(max_length=3, choices=ADMIN_TYPE)
