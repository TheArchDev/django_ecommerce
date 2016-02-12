from products.models import Product
from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

#think could have either .models or products.models
from .models import Order
from django.http import HttpResponse


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
	paginator = Paginator(all_products,5)

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

def add_to_cart(request, product_id):
	print "auth",request.user.is_authenticated()
	if request.user.is_authenticated():
		#request is an object. request.user is an object
		# 1. only returns orders that are the current user's 
		# 2. only returns orders that are active (status=1)
		orders=Order.objects.filter(user=request.user,status=1)
		# SELECT * FROM product_order WHERE user_id = 1 AND status = 1;
		#orders is an array that sometimes contains an object
		# if there are no active orders for the current user
		if len(orders) == 0:
			# creates the order that is active and associated with the current user
			order=Order(status=1, user=request.user)
			order.save()
			# INSERT INTO product_order (user_id, status) VALUES (eg1,1);
			# grab product instance from products that has the right id
			product = Product.objects.get(id=product_id)
			# SELECT * FROM product_product WHERE id = 1;

			# adds product instance to current user's active order instance
			order.items.add(product)
			# INSERT INTO product_order_item (product_id,order_id) VALUES (1,1);

			#return HttpResponse("An open order did not exist. We created a new order and added the product to it.")
			print "Signal 1"
			return redirect("/products/cart")

		# if the current user already has an active order
		else:
			# get user's active order instance out of array
			order = orders[0]
			#get the product
			product = Product.objects.get(id=product_id)
			#add 2 user's active order instance
			order.items.add(product)
			
			#return HttpResponse("An open order already existed, we added a product to that open order.")
			print "Signal 2"
			return redirect("/products/cart")

	return redirect("/login")

def remove_from_cart(request, product_id):
	print "product_id", product_id

	orders = Order.objects.filter(user=request.user,status=1)
	order = orders[0]
	order.save()
	order.items.remove(product_id)

	#return HttpResponse("Clicked to remove item from cart")
	return redirect("/products/cart")

def cart(request):
	if not request.user.is_authenticated():
		print "Trigger cart login"
		return redirect("/login")
	
	#Need to add in an if statement such that if browser comes to this site without having placed an order

	orders = Order.objects.filter(user=request.user,status=1)

	order = orders[0]
	order.save()

	order_items = order.items.all()

	cart_total=sum([order_item.price for order_item in order_items])

	return render(request,"products/cart.html", {"order_items": order_items, "cart_total":cart_total})
	#return HttpResponse("You're successfully logged into your cart")




