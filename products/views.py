from products.models import Product
from django.shortcuts import render,redirect

def index(request):
	all_products = Product.objects.all()
	return render(request,'products/index.html', {'products': all_products})

def product_page(request,id):
	p = Product.objects.get(pk=id)
	return render(request,'products/product.html', {'product': p})
