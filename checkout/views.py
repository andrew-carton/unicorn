from django.shortcuts import render, reverse, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from django.conf import settings
from django.utils import timezone
from issues.models import Ticket, Vote
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request, pk=None):
	total = 50
	feature = get_object_or_404(Ticket, pk=pk) if pk else None
	if request.method=="POST":
		order_form = OrderForm(request.POST)
		payment_form = MakePaymentForm(request.POST)
		
		if order_form.is_valid() and payment_form.is_valid():
			order = order_form.save(commit=False)
			order.date = timezone.now()
			order.save()
			
			
			
			try:
				customer = stripe.Charge.create(
					amount = int(total * 100),
					currency = "EUR",
					description = request.user.email,
					card = payment_form.cleaned_data['stripe_id'],
				)
			except stripe.error.CardError:
				messages.error(request, "Your card was declined!")
				
			if customer.paid:
				messages.error(request, "You have successfully paid")
				if feature:
					feature.votes = feature.votes + 1
					feature.save()
					v = Vote(ticket=feature, user=request.user)
					v.save()
				return redirect(reverse('features'))
			else:
				messages.error(request, "Unable to take payment")
		else:
			print(payment_form.errors)
			messages.error(request, "We were unable to take a payment with that card!")
	else:
		payment_form = MakePaymentForm()
		order_form = OrderForm()
		
	return render(request, "checkout.html", { 'order_form': order_form, 'payment_form' : payment_form, 'publishable': settings.STRIPE_PUBLISHABLE, 'total': total, 'feature': feature})
	
				