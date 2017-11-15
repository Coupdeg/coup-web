from django.db import models
import datetime
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from .storage import ImgurStorage

STORAGE = ImgurStorage()

class User(models.Model):
	email = models.EmailField(max_length=50, unique=True)
	password = models.CharField(max_length=256)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=50)
	def __str__(self):
		return 'ID : %s -> Email : %s' % (self.id, self.email)

class Product(models.Model):
	types = (
		('0', 'Bags'),
		('1', 'Soaps'),
		('2', 'Dresses'),
		('3', 'Shirts'),
		('4', 'Scarves'),
		('5', 'Accessories')
	)
	name = models.CharField(max_length=50)
	details = models.CharField(max_length=150)
	product_types = models.CharField(max_length=1, choices=types)
	price = models.IntegerField()
	def __str__(self):
		return 'ID : %s -> Name : %s' % (self.id, self.name)

class Image(models.Model):
	types = (
		('0', 'user'),
		('1', 'product')
	)
	types_role = (
		('0', 'main image'),
		('1', 'sub image')
	)
	image = models.ImageField(upload_to='photos', storage=STORAGE, null=True, blank=True)
	image_types = models.CharField(max_length=1, choices=types)
	type_id = models.IntegerField()
	role = models.CharField(max_length=1, choices=types_role, default=0)

	def __str__(self):
		return 'ID : %s -> Type : %s -> Type ID : %s' % (self.id, self.image_types, self.type_id)

class History(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product)
	date = models.DateTimeField('date published',null=True)

	def __str__(self):
		return 'User : %s -> Product : %s -> Date : %s' % (self.user.email, self.product.name, self.date)

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Cart(models.Model):
	creation_date = models.DateTimeField(verbose_name=_('creation date'))
	checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

	class Meta:
		verbose_name = _('cart')
		verbose_name_plural = _('carts')
		ordering = ('-creation_date',)
	
	def __unicode__(self):
		return unicode(self.creation_date)

class ItemManager(models.Manager):
	def get(self, *args, **kwargs):
		if 'product' in kwargs:
			kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
			kwargs['object_id'] = kwargs['product'].pk
			del(kwargs['product'])
		return super(ItemManager, self).get(*args, **kwargs)

class Item(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=_('cart'))
	quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
	unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()

	objects = ItemManager()

	class Meta:
		verbose_name = _('item')
		verbose_name_plural = _('items')
		ordering = ('cart',)
	
	def __unicode__(self):
		return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

	def total_price(self):
		return self.quantity * self.unit_price
	total_price = property(total_price)

	def get_product(self):
		return self.content_type.get_object_for_this_type(pk=self.object_id)

	def set_product(self, product):
		self.content_type = ContentType.objects.get_for_model(type(product))
		self.object_id = product.pk
	
	product = property(get_product, set_product)
