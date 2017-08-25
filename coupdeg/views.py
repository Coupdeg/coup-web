from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .models import Product
from .models import User
from passlib.hash import django_pbkdf2_sha256 as handler

def landing(request):
			products = Product.objects.all().order_by('-id')[:6]
			images = Image.objects.filter(image_types = 1).order_by('-type_id')[:6]
			context = {
				'products': products,
				'images': images
			}
			return render(request, 'landing/index.html', context)

def product(request):
	all_images = Image.objects.all()
	context = {
		'all_images': all_images,
	}
	return render(request, 'product/index.html', context)

def about(request):
	return render(request, 'about/index.html')

def login(request):
	return render(request, 'user/login.html')

def register(request):
	return render(request, 'user/register.html')

def user(request):
	if request.method == 'POST':
		password = request.POST['password']
		re_password = request.POST['re-password']

		if password == re_password and password != '':
			email = request.POST['email']
			password = handler.hash(password)
			first_name = request.POST['firstname']
			last_name = request.POST['lastname']
			address = request.POST['address']
			city = request.POST['city']
			state = request.POST['state']
			country = request.POST['country']
			zip_code = request.POST['zip']
			user = User(email=email, password=password,first_name=first_name, last_name=last_name,
									address=address, city=city, state=state, country=country, zip_code=zip_code)
			user.save()
			return redirect('/user/login')	