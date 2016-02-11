from products.models import Product
from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



def index(request):
	all_products = Product.objects.all()

	search = request.GET.get('search')
	print "search",search

	priceless = request.GET.get('priceless')
	print "priceless", priceless

	pricemore = request.GET.get('pricemore')
	print "pricemore", pricemore

	#import the Q lets us do 'or's . In this case we want searches to be returned if the searched word appears in the name OR the description, rather than having to appear in both
	#the i indicates case insensitive
	if search:
		all_products = all_products.filter(Q(name__icontains=search) | Q(description__icontains=search))

	if priceless and pricemore:
		print "Branch 3"
		all_products = all_products.filter(price__lte=priceless,price__gte=pricemore)
	elif priceless:
		print "Branch 1"
		all_products = all_products.filter(price__lte=priceless)
	elif pricemore:
		print "Branch 2"
		all_products = all_products.filter(price__gte=pricemore)

	#alternatively could have done two separate if statements. One to check for pricemore, then the altered all_products out of that can feed into the next if statement which will check for priceless, before amending all_products as appropriate

	#it's saying 10 max
	paginator = Paginator(all_products,10)

	#Line below is basically saying get this value out of the dictionary.
	#request.GET is like/derived from a dictionary. This is to do with the HTTP GET, operating on the string.
	#then .get() can be done on any dictionary. If it's not found, then it just return None. Whereas if did dict[] with square brackets, would have to be try-exception rules etc.
	page = request.GET.get('page')
	print "GETREQUEST:", request.GET
	print "PAGENUM:", page


	try:
		all_products = paginator.page(page)
	except PageNotAnInteger:
		all_products = paginator.page(1)
	except EmptyPage:
		all_products = paginator.page(paginator.num_pages)

	return render(request,'products/index.html', {'products': all_products})

def product_page(request,id):
	p = Product.objects.get(pk=id)
	return render(request,'products/product.html', {'product': p})
