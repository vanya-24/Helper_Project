from django.shortcuts import render,HttpResponse,redirect
from covid_helper.models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
	return render(request, 'covid_helper/home.html')

def about(request):
	return render(request,'covid_helper/abts.html')

def registration(request):
	return render(request,'covid_helper/registration.html')

def appointment(request):
	return render(request,'covid_helper/appointment.html')

def doctors(request):
	return render(request,'covid_helper/doctors.html')


def contact(request):
	messages.success(request, 'Welcome to contact')
	if request.method=='POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		content = request.POST['content']

		if len(name)<2 or len(phone)<10 or len(email)<3 or len(content)<4:
			messages.error(request, "Please fill the form correctly")
		else:
			messages.success(request, "Successfully submitted")
		contact = Contact(name=name, email=email, phone=phone, content=content)
		contact.save()
	return render(request,'covid_helper/contact.html')

def resources(request):
	messages.success(request, 'Welcome to resources')
	return render(request, 'covid_helper/resources.html')

def handleSignup(request):
	if request.method == 'POST':
		# Get the post parameters
		username = request.POST['username']
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']


		if len(username) > 10:
			messages.error(request, 'Username must be under 10')
			return redirect('/')

		if not username.isalnum():
			messages.error(request, 'Username must be alphanumeric')
			return redirect('/')

		if pass1 != pass2:
			messages.error(request, 'Passwords do not match')
			return redirect('/')
		

		myuser = User.objects.create_user(username,email,pass1)
		myuser.fname = fname
		myuser.lname = lname
		myuser.save()
		messages.success(request, 'Account registered successfully')
		return redirect('/')
	else:
		return HttpResponse('404-Not Found');


def handleLogin(request):
	if request.method == 'POST':
		loginusername = request.POST['loginusername']
		loginpassword = request.POST['loginpassword']

		user = authenticate(username=loginusername, password=loginpassword)

		if user is not None:
			login(request, user)
			messages.success(request, "Successfully Logged in")
			return redirect('/')
		else:
			messages.error(request, "Invalid Credentials,Please try again")
			return redirect('/')
	return HttpResponse('404 - Not Found')

def handlelogout(request):
	logout(request)
	messages.success(request,"Successfully Logged Out")
	return redirect('/')
