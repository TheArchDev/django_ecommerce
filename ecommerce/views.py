from django.shortcuts import render

from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


def register(request):
	#If user is not attempting to POST with their request, load up the register webpage
	if request.method == 'GET' or request.method != 'POST':
			return render(request, 'ecommerce/register.html', {})

	#Otherwise, print user's post request to the terminal log
	#print request.POST
	#Create a new user using built in django user libraries, pulling information from their POST request
	user = User.objects.create_user(username = request.POST['user_name'], email = request.POST['email'], password = request.POST['password'])
	#If we are not successful in generating a user, reload the register webpage.
	#if not user:
		#return render(request, 'ecommerce/register.html', {})
	#Otherwise, we save the new user instance
	#user.save()
	#And then we log the user in.
	user = authenticate(username=request.POST['user_name'],password=request.POST['password'])
	login(request, user)
	#Finally, we redirect to the homepage if we were successful in registering a new user. There is now a logged in user.
	return redirect('/')


def home(request):
	return render(request, 'ecommerce/home.html', {})

def login_user(request):

	print "trigger1", request.user

	if request.method == 'GET' or request.method != 'POST':
		print "trigger2", request.user
		return render(request, 'ecommerce/login.html', {})

	user = authenticate(username = request.POST['user_name'], password = request.POST['password'])

	if not user:
		return redirect('/login')

	login(request, user)

	print "trigger3", request.user

	return redirect('/')

def logout_user(request):
	print "trigger4", request.user
	logout(request)
	print "trigger5", request.user

	return redirect('/')
