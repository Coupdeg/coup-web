from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .models import Product

def landing(request):
	products = Product.objects.all().order_by('-id')[:6]
	images = Image.objects.filter(image_types = 1).order_by('-type_id')[:6]
	context = {
		'products': products,
		'images': images
	}

 	return render(request, 'landing/index.html', context)

def detail(request):
	return render(request, 'detail/index.html')

def about(request):
	return render(request, 'about/index.html')