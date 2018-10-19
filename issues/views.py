from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ticket
from .forms import TicketForm


def tickets(request):
	mytickets = Ticket.objects.all().order_by('-created_on')
	return render(request, "tickets.html", {"tickets" : mytickets})
	
def create_or_edit_ticket(request, pk=None):
	post = get_object_or_404(Ticket, pk=pk) if pk else None
	if request.method == "POST":
		form = TicketForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save()
			return redirect(tickets)
	else:
		form = TicketForm(instance=post)
	return render(request, 'ticketform.html', {'form': form})
	
	