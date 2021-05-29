from django.shortcuts import render,HttpResponse
from covid_helper.models import Contact
from django.contrib import messages

def home(request):
	return render(request, 'covid_helper/home.html')

def about(request):
	messages.success(request, "This is about")
	return render(request,'covid_helper/about.html')

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

