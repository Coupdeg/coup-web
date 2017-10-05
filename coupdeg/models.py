from django.db import models
import datetime
from django.utils import timezone

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
	image = models.ImageField(blank=True)
	image_types = models.CharField(max_length=1, choices=types)
	type_id = models.IntegerField()
	role = models.CharField(max_length=1, choices=types_role, default=0)

	def __str__(self):
		return 'ID : %s -> Type : %s -> Type ID : %s' % (self.id, self.image_types, self.type_id)

class History(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product)
	date = models.DateTimeField('date published',null=True)

	# def __str__(self):
	# 	return 'Product : %s -> Date : %s' % (self.product.name, self.date)

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

