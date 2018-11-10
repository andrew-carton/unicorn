from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from .models import Ticket, Comment, Vote
from .forms import TicketForm, CommentForm, TicketFormEdit
import json

def bugs(request):
	ticketdict = {}
	
	mytickets = Ticket.objects.all().order_by('-created_on')
	for t in mytickets:
		if t.feature == Ticket.FEATURE:
			continue
		ticketdict[t.id] = []
		ticketdict[t.id].append(t)
		votes = Vote.objects.all().filter(ticket=t, user=request.user)
		if votes:
			ticketdict[t.id].append(True)
		else:
			ticketdict[t.id].append(False)
		
	args = {}
	
	args["tickets"] = ticketdict
	args["votes"] = votes
	args["user"] = request.user
	
	return render(request, "bugs.html", args)

def bug(request, pk=None):
	bug = get_object_or_404(Ticket, pk=pk) if pk else None
	comments = Comment.objects.all().filter(ticket=bug)
	
	
	return render(request, "bug.html", {'bug' : bug, "comments": comments})
	
	
def create_ticket(request, pk=None):
	post = get_object_or_404(Ticket, pk=pk) if pk else None
	mytickets = Ticket.objects.all().order_by('-created_on')
	if request.method == "POST":
		form = TicketForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save()
			return redirect(tickets)
	else:
			
		form = TicketForm({'created_by': request.user})
	comments = Comment.objects.all().filter(ticket=post)
	create = True
	
	return render(request, 'ticketform.html', {'form': form, "comments" : comments, "ticket": post, "create": create})
	
def edit_ticket(request, pk=None):
	post = get_object_or_404(Ticket, pk=pk) if pk else None
	mytickets = Ticket.objects.all().order_by('-created_on')
	if request.method == "POST":
		form = TicketFormEdit(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save()
			return redirect(bugs)
	else:
		form = TicketFormEdit(instance=post)
	comments = Comment.objects.all().filter(ticket=post)
	create = False
	return render(request, 'ticketform.html', {'form': form, "comments" : comments, "ticket": post, "create": create})
	
def create_comment(request):
	data = json.loads(request.body)
	ticket = get_object_or_404(Ticket, pk=data['id'])
	comment = Comment.objects.create(ticket=ticket, comment=data['comment'], created_by=request.user)
	return HttpResponse('') 
	

def vote(request, pk = None):
	ticket = get_object_or_404(Ticket, pk=pk) if pk else None
	if ticket:
		ticket.votes = ticket.votes + 1
		ticket.save()
		v = Vote(ticket=ticket, user=request.user)
		v.save()
	return redirect(bugs)

	
	