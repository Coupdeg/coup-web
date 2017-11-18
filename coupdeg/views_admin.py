from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from models import Image, Product

def index(request):
	return render(request, 'user/admin/index.html')

def add_product(request):
	if request.method == 'POST':
		image = request.FILES.get('image', False)
		name = request.POST.get('name', False)	
		details = request.POST.get('details', False)
		product_types = request.POST.get('type', False)
		price = request.POST.get('price', False)
		product = Product(name=name, details=details, product_types=product_types, price=price)
		product.save()
		image = Image(image=image, image_types=1, type_id=product.id, role=0)
		image.save()						

	return render(request, 'user/admin/product/add.html')

def show_product(request):
	products = Product.objects.all()
	context = {
		'products': products,
	}
	return render(request, 'user/admin/product/show.html', context)

def delete_product(request):
	products = Product.objects.all()
	context = {
		'products': products,
	}
	if request.method == 'GET':
		return render(request, 'user/admin/product/delete.html', context)
	else:
		products = request.POST.getlist('product')
		for pk in products:
			Product.objects.get(pk=pk).delete()
			Image.objects.filter(image_types = 1, type_id = pk).delete()	
		return render(request, 'user/admin/product/delete.html', context)

def edit_product(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'user/admin/product/edit.html', { 'product': product })


def product(request):
	return render(request, 'user/admin/product/index.html')
