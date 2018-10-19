from django.shortcuts import render
from .models import Ticket

def tickets(request):
	mytickets = Ticket.objects.all()
	return render(request, "tickets.html", {"tickets" : mytickets})
	
