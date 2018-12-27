from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm, UserRegistrationForm
from issues.models import Ticket


"""
    The Account information displaying the tickets created
"""


def account_info(request):

    # Order tickets by created_on
    mytickets = Ticket.objects.all().order_by('-created_on')

    return render(request, "account_info.html", {'tickets' : mytickets })


"""
	Logout the user and send a message
"""


def logout(request):
    # Logout
    auth.logout(request)
    # Send message success
    messages.success(request, "You have successfully been logged out!")
    # Send the user to the home page
    return redirect(reverse('home'))


"""
	Login the user with a valid username and password with messages
	indicating any validation errors.
"""


def login(request):
    # Login form
    login_form = UserLoginForm(request.POST)

    # see if login form validates correctly
    if login_form.is_valid():
        # Authenticate with the valid information
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        # send success message
        messages.success(request, "You have successfully logged in")

        # Test to see if a user was authenticated correctly
        if user:
            # Login user
            auth.login(user=user, request=request)
            # Redirect user to home page
            return redirect(reverse('home'))
        else:
                # Give message because authentication failed
            login_form.add_error(
                None, "Your username and password is incorrect")

    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


"""
	This is the registration view
"""


def registration(request):
    # See if user is autenthicated already - then send them home
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == "POST":
        # Registration form
        registration_form = UserRegistrationForm(request.POST)

        # Test if validated correctly
        if registration_form.is_valid():
            registration_form.save()
            # Authenticate user with password
            user = auth.authenticate(
                username=request.POST['username'], password=request.POST['password1'])

            # Test if user authenticated correctly
            if user:
                        # login
                auth.login(user=user, request=request)
                # success message send
                messages.success(request, "You have successfully registered")
                return redirect(reverse('home'))
            else:
                        # error message if not authenticated
                messages.error(
                    request, "Unable to register your account at this time")
    else:
        # display empty registration form
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {"registration_form": registration_form})
