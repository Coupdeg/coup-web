from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .models import Product

def product(request, type_number):
	type_number = int(type_number)
	if type_number == 1:
		products = Product.objects.filter(product_types = 0)
	elif type_number == 2:
		products = Product.objects.filter(product_types = 1)
	elif type_number == 3:
		products = Product.objects.filter(product_types = 2)
	elif type_number == 4:
		products = Product.objects.filter(product_types = 3)
	elif type_number == 5:
		products = Product.objects.filter(product_types = 4)
	elif type_number == 6:
		products = Product.objects.filter(product_types = 5)
	else :
		products = Product.objects.all()
		
	images = Image.objects.filter(image_types = 1).order_by('type_id')
	context = {
		'images': images,
		'products': products,
	}
	return render(request, 'product/index.html', context)

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	image = Image.objects.filter(type_id = product_id)[0]
	return render(request, 'product/detail.html', { 'product': product, 'image': image })