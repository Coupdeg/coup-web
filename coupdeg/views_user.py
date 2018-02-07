from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User, Product, History, Payment, Image
from .cart import Cart
from django.utils import timezone
from passlib.hash import django_pbkdf2_sha256 as handler

def login(request):
	if request.method == 'POST':
		if request.POST['type'] == 'Logout':
			request.session['email'] = None
			return redirect('/')						
		else:	
			password = request.POST['password']
			user = User.objects.filter(email = request.POST['email'])
			if user and handler.verify(password, user[0].password) == True :
				request.session['email'] = user[0].email
				return redirect('/')
			else :
				error = "Invalid email or password ."
				context = {
					'error': error
				}	
				return render(request, 'user/login.html', context)
	elif request.method == 'DELETE':
		request.session['email'] = None
		return redirect('/')
	else:
		error = None
		context = {
			'error': error
		}	
		return render(request, 'user/login.html', context)

def register(request):
	if request.method == 'POST':
		error = []
		email = request.POST['email']
		if email == '':
			error.append("email")
		password = request.POST['password']
		re_password = request.POST['re-password']
		if password == re_password and password != '':
			password = handler.hash(password)
		else:
			error.append("password")
		first_name = request.POST['firstname']
		if first_name == '':
			error.append('first_name')
		last_name = request.POST['lastname']
		if last_name == '':
			error.append('last_name')
		address = request.POST['address']
		if address == '':
			error.append('address')
		city = request.POST['city']
		if city == '':
			error.append('city')
		state = request.POST['state']
		if state == '':
			error.append('state')
		country = request.POST['country']
		if country == '':
			error.append('country')
		zip_code = request.POST['zip']
		if zip_code == '':
			error.append('zip_code')
		phone = request.POST['phone']
		if phone == '':
			error.append('phone')
		user = User(email=email, password=password,first_name=first_name, last_name=last_name,
								address=address, city=city, state=state, country=country, zip_code=zip_code,
								phone=phone)
		if error:
			context = {
				'error': error,
				'email': email or None,
				'first_name': first_name or None,
				'last_name': last_name or None,
				'address': address or None,
				'city': city or None,
				'state': state or None,
				'country': country or None,
				'zip_code': zip_code or None,
				'phone': phone or None
			}	
			return render(request, 'user/register.html', context) 
		else:
			user.save()
			return redirect('/user/login')
	else :
			return render(request, 'user/register.html')

def user(request):
		user_id = User.objects.filter(email = request.session['email'])
		user = get_object_or_404(User, pk=user_id[0].id)
		context = {
			'user': user
		}		
		if request.method == 'POST':
			user.email = request.POST['email']
			user.first_name = request.POST['firstname']
			user.last_name = request.POST['lastname']
			user.address = request.POST['address']
			user.city = request.POST['city']
			user.state = request.POST['state']
			user.country = request.POST['country']
			user.zip_code = request.POST['zip']
			user.phone = request.POST['phone']
			user.save()

		return render(request, 'user/profile.html', context)

def history(request):
	if request.method == 'POST':
		user_id = User.objects.filter(email = request.POST['email'])
		user = get_object_or_404(User, pk=user_id[0].id)		
		now = timezone.now()
		history = History(user=user, date=now)
		history.save()
		return redirect('/product/'+product_id)
	else:
		if request.session['email']:
			user_id = User.objects.filter(email = request.session['email'])
			user = get_object_or_404(User, pk=user_id[0].id)
			history = History.objects.filter(user = user)
			payment = []
			for h in history :
				payment.append(Payment.objects.filter(history=h))

			context = {
				'payment': payment,
			}	
			return render(request, 'user/history.html', context)
		else :
			return redirect('/user/login')

def checkout(request):
	if request.method == 'POST':
		cart = Cart(request)
		user = User.objects.get(email = request.session['email'])
		image = request.FILES.get('image-payment', False)
		now = timezone.now()
		history = History(user=user, date=now)
		history.save()
		for item in cart:
			product = Product.objects.get(name = item.product.name)
			quantity = item.quantity
			payment = Payment(history=history, product=product, quantity=quantity)
			payment.save()
		cart.clear()
		image = Image(image=image, image_types=2, type_id=history.id, role=0)
		image.save()
	return render(request, 'user/checkout.html')