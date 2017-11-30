from django.http import Http404, HttpResponse
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Image
from .models import Product, Item
from .cart import Cart

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

	paginator = Paginator(products, 12)
	page = request.GET.get('page')
	try:
			products = paginator.page(page)
	except PageNotAnInteger:
			products = paginator.page(1)
	except EmptyPage:
			products = paginator.page(paginator.num_pages)
		
	images = Image.objects.filter(image_types = 1).order_by('type_id')
	context = {
		'images': images,
		'products': products,
		'product_types': type_number-1
	}
	return render(request, 'product/index.html', context)

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	image = Image.objects.filter(type_id = product_id)[0]
	return render(request, 'product/detail.html', { 'product': product, 'image': image })

def add_to_cart(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	cart = Cart(request)
	cart.add(product, product.price)
	return redirect(request.META['HTTP_REFERER'])

def remove_from_cart(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	cart = Cart(request)
	cart.remove(product)
	return redirect(request.META['HTTP_REFERER'])

def update_from_cart(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	cart = Cart(request)
	if request.POST.get('type', False) == "+" :
		quantity = cart.get_quantity_item(product) + 1
	else :
		quantity = cart.get_quantity_item(product) - 1
	cart.update(product, quantity)
	return redirect(request.META['HTTP_REFERER'])

def search(request):
	type_number = 1
	name = request.POST.get('search_input')
	products = Product.objects.filter(name__contains=name)
	paginator = Paginator(products, 12)
	page = request.GET.get('page')
	try:
			products = paginator.page(page)
	except PageNotAnInteger:
			products = paginator.page(1)
	except EmptyPage:
			products = paginator.page(paginator.num_pages)
	context = {
		'products': products,
		'product_types': type_number-1
	}
	return render(request, 'product/index.html', context)
 
