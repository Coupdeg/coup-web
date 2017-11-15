from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
	return render(request, 'user/admin/index.html')