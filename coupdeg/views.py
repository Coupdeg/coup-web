from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .models import User

def landing(request):
 	return render(request, 'landing/index.html')

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

		if password == re_password:
			email = request.POST['email']
			first_name = request.POST['firstname']
			last_name = request.POST['lastname']
			address = request.POST['address']
			city = request.POST['city']
			state = request.POST['state']
			country = request.POST['country']
			zip_code = request.POST['zip']
			user = User(email=email, first_name=first_name, last_name=last_name,
									address=address, city=city, state=state, country=country, zip_code=zip_code)
			user.save()
			return redirect('/user/login')
	