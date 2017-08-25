from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Image

def landing(request):
 	return render(request, 'landing/index.html')

def product(request):
	all_images = Image.objects.all()
	context = {
		'all_images': all_images,
	}
	return render(request, 'product/index.html', context)

def detail(request):
	return render(request, 'about/detail.html')

def about(request):
	return render(request, 'about/index.html')

def login(request):
	return render(request, 'user/login.html')