from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ticket, Comment
from .forms import TicketForm, CommentForm


def tickets(request):
	mytickets = Ticket.objects.all().order_by('-created_on')
	return render(request, "tickets.html", {"tickets" : mytickets})
	
def create_or_edit_ticket(request, pk=None):
	post = get_object_or_404(Ticket, pk=pk) if pk else None
	mytickets = Ticket.objects.all().order_by('-created_on')
	if request.method == "POST":
		form = TicketForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save()
			return redirect(tickets)
	else:
		form = TicketForm(instance=post)
	comments = Comment.objects.all().filter(ticket=post)
	return render(request, 'ticketform.html', {'form': form, "comments" : comments})
	

def create_comment(request, pk=None):
	post = get_object_or_404(Comment, pk=pk) if pk else None
	mytickets = Comment.objects.all()
	if request.method == "POST":
		form = CommentForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save()
			return redirect(tickets)
	else:
		form = CommentForm(instance=post)
	
	return render(request, 'commentform.html', {'form': form})
	

	
	