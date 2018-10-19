from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm, UserRegistrationForm


	
def logout(request):
	auth.logout(request)
	messages.success(request, "You have successfully been logged out!")
	return redirect(reverse('home'))
	
def login(request):
	login_form = UserLoginForm(request.POST)
	
	if login_form.is_valid():
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		messages.success(request, "You have successfully logged in")
	
		if user:
			auth.login(user=user, request=request)
		else:
			login_form.add_error(None, "Your username and password is incorrect")
			
	else:
		login_form = UserLoginForm()
	return render(request, 'login.html', {"login_form" : login_form})
	
def registration(request):
	if request.user.is_authenticated:
		return redirect(reverse('home'))
	
	if request.method == "POST":
		registration_form = UserRegistrationForm(request.POST)
		
		if registration_form.is_valid():
			registration_form.save()
		
			user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
		
			if user:
				auth.login(user=user, request=request)
				messages.success(request, "You have successfully registered")
				return redirect(reverse('home'))
			else:
				messages.error(request, "Unable to register your account at this time")
	else:	
		registration_form = UserRegistrationForm()
	return render(request, 'registration.html', {"registration_form": registration_form})
	
	