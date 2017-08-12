from django.db import models

class User(models.Model):
	email = models.EmailField(max_length=50, unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=50)

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
	product_type = models.CharField(max_length=1, choices=types)
	price = models.IntegerField()
