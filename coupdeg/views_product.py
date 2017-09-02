from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .models import Product

def product(request):
	images = Image.objects.filter(image_types = 1).order_by('-type_id')
	products = Product.objects.all()
	context = {
		'images': images,
		'products': products,
	}
	return render(request, 'product/index.html', context)

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	image = Image.objects.filter(type_id = product_id)[0]
	return render(request, 'product/detail.html', { 'product': product, 'image': image })