from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from passlib.hash import django_pbkdf2_sha256 as handler

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
		else :
			return redirect('/')