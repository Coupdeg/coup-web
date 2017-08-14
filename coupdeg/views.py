from django.http import Http404
from django.shortcuts import render, get_object_or_404

def landing(request):
 	return render(request, 'landing/index.html')

def product(request):
	return render(request, 'product/index.html')

def about(request):
	return render(request, 'about/index.html')