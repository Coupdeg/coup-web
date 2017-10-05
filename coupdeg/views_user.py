from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User
from .models import Product
from .models import History
from django.utils import timezone
from passlib.hash import django_pbkdf2_sha256 as handler

def login(request):
	if request.method == 'POST':
		if request.POST['type'] == 'LOGOUT':
			request.session['email'] = None
			return redirect('/')						
		else:	
			password = request.POST['password']
			user = User.objects.filter(email = request.POST['email'])
			if user and handler.verify(password, user[0].password) == True :
				request.session['email'] = user[0].email
				return redirect('/')
			else :
				return redirect('/user/register')
	elif request.method == 'DELETE':
		request.session['email'] = None
		return redirect('/')
	else:
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

def history(request):
	if request.method == 'POST':
		user_id = User.objects.filter(email = request.POST['email'])
		print(request.POST['email'])
		user = get_object_or_404(User, pk=user_id[0].id)		
		product_id = request.POST['product_id']
		product = get_object_or_404(Product, pk=product_id)
		now = timezone.now()
		history = History(user=user, product= product, date=now)
		history.save()
		return redirect('/product/'+product_id)
	else:	
		return render(request, 'user/history.html')

def post_history(request):
		product_id = request.GET.get('product_id')
		product = get_object_or_404(Product, pk=product_id)
		now = timezone.now()
		history = History(product= product, date=now)
		history.save()