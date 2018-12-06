from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from .models import Ticket, Comment, Vote
from .forms import TicketForm, TicketFormEdit
import json

# Bugs view request


def bugs(request):
    # Create a ticket holding the votes and tickets together
    ticketdict = {}

    # Order tickets by created_on
    mytickets = Ticket.objects.all().order_by('-created_on')

    # Iterate through tickets
    for t in mytickets:
        if t.feature == Ticket.FEATURE:
            continue
        ticketdict[t.id] = []
        ticketdict[t.id].append(t)
        # Get vote for ticket object
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

# The features view request


def features(request):
    # Ticket dictionary to hold tickets-votes
    ticketdict = {}

    # Get all tickets, sorted by created on
    mytickets = Ticket.objects.all().order_by('-created_on')

    # for all tickets append the vote and ticket together
    for t in mytickets:
        if t.feature != Ticket.FEATURE:
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

    return render(request, "features.html", args)


# Bug view request
def bug(request, pk=None):
    bug = get_object_or_404(Ticket, pk=pk) if pk else None

    # Get all comments associated with bug
    comments = Comment.objects.all().filter(ticket=bug)

    return render(request, "bug.html", {'bug': bug, "comments": comments})


# Feature view request
def feature(request, pk=None):
    feature = get_object_or_404(Ticket, pk=pk) if pk else None

    # Get all comments associated with feature
    comments = Comment.objects.all().filter(ticket=feature)

    return render(request, "feature.html", {'feature': feature, "comments": comments})


# Create ticket view request
def create_ticket(request, pk=None):
    post = get_object_or_404(Ticket, pk=pk) if pk else None

    # Sort tickets by created -on
    mytickets = Ticket.objects.all().order_by('-created_on')
    if request.method == "POST":
        # Create the ticket form
        form = TicketForm(request.POST, request.FILES, instance=post)

        # Test if valid and save and redirect home
        if form.is_valid():
            post = form.save()
            return redirect(reverse('home'))
    else:

        form = TicketForm({'created_by': request.user})

        # Get all comments
    comments = Comment.objects.all().filter(ticket=post)

    # Set to true for this page
    create = True

    return render(request, 'ticketform.html', {'form': form, "comments": comments, "ticket": post, "create": create})

# Edit ticket request


def edit_ticket(request, pk=None):
    post = get_object_or_404(Ticket, pk=pk) if pk else None
    # Get all tickets by created_on
    mytickets = Ticket.objects.all().order_by('-created_on')

    if request.method == "POST":
        # Get ticket form edit box
        form = TicketFormEdit(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(reverse('home'))
    else:
        form = TicketFormEdit(instance=post)

        # Get all comments
    comments = Comment.objects.all().filter(ticket=post)
    create = False
    return render(request, 'ticketform.html', {'form': form, "comments": comments, "ticket": post, "create": create})


# Create comment request view
def create_comment(request):
    # Load data from JSON
    data = json.loads(request.body)
    ticket = get_object_or_404(Ticket, pk=data['id'])

    # Create comment
    comment = Comment.objects.create(
        ticket=ticket, comment=data['comment'], created_by=request.user)
    return HttpResponse('')


# Vote request view
def vote(request, pk=None):
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if ticket:
        # Increment votes now
        ticket.votes = ticket.votes + 1
        ticket.save()
        # Create a ticket-user entry
        v = Vote(ticket=ticket, user=request.user)
        v.save()
    return redirect(bugs)
