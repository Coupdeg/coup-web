from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .models import Product

def product(request):
	all_images = Image.objects.all()
	context = {
		'all_images': all_images,
	}
	return render(request, 'product/index.html', context)

def details(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	image = Image.objects.filter(type_id = product_id)[0]
	return render(request, 'product/details.html', { 'product': product, 'image': image })