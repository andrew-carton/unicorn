from django.shortcuts import render
from django.http import JsonResponse
from issues.models import Ticket
import datetime

def graphs(request):
	return render(request, 'graphs.html')

def progress(request):
	data = []

	
	mytickets = Ticket.objects.all()
	
	for ticket in mytickets:
		found = 0
		for i in data:
			if i['progress'] == ticket.status:
				i['amount'] = i['amount'] + 1
				found = 1
				break
			else:
				found = 0
				
		if found == 0:
			progress = dict()
			progress['progress'] = ticket.status
			progress['amount'] = 1
			data.append(progress)
			


	return JsonResponse(data, safe=False)
	
def daily(request):
	data = []
	mytickets = Ticket.objects.all()
	today = datetime.date.today()
	week_ago = today - datetime.timedelta(days=7)
	
	
	current = week_ago
	
	daily = {}
	daily['day'] = "Mon"
	daily['amount'] = 0
	data.append(daily)
	
	daily = {}
	daily['day'] = "Tue"
	daily['amount'] = 0
	data.append(daily)
	
	daily = {}
	daily['day'] = "Wed"
	daily['amount'] = 0
	data.append(daily)
	
	daily = {}
	daily['day'] = "Thu"
	daily['amount'] = 0
	data.append(daily)
	
	daily = {}
	daily['day'] = "Fri"
	daily['amount'] = 0
	data.append(daily)
	
	daily = {}
	daily['day'] = "Sat"
	daily['amount'] = 0
	data.append(daily)
	
	daily = {}
	daily['day'] = "Sun"
	daily['amount'] = 0
	data.append(daily)
	
	
	for ticket in mytickets:
		if ticket.closed_on == None:
			continue
			
		ticketdate = ticket.closed_on.date()
		if (ticketdate >= week_ago and ticketdate <= today):
			if ticketdate.weekday() == 0:
				for i in data:
					if i['day'] == "Mon":
						i['amount'] = i['amount'] + 1
			elif ticketdate.weekday() == 1:
				for i in data:
					if i['day'] == "Tue":
						i['amount'] = i['amount'] + 1
			elif ticketdate.weekday() == 2:
				for i in data:
					if i['day'] == "Wed":
						i['amount'] = i['amount'] + 1
			elif ticketdate.weekday() == 3:
				for i in data:
					if i['day'] == "Thu":
						i['amount'] = i['amount'] + 1
			elif ticketdate.weekday() == 4:
				for i in data:
					if i['day'] == "Fri":
						i['amount'] = i['amount'] + 1
			elif ticketdate.weekday() == 5:
				for i in data:
					if i['day'] == "Sat":
						i['amount'] = i['amount'] + 1
			elif ticketdate.weekday() == 6:
				for i in data:
					if i['day'] == "Sun":
						i['amount'] = i['amount'] + 1
						
	
	return JsonResponse(data, safe=False)
	
	
def weekly(request):
	data = []
	mytickets = Ticket.objects.all()
	today = datetime.date.today()
	
	one_week_ago = today - datetime.timedelta(days=7)
	two_weeks_ago = today - datetime.timedelta(days=14)
	three_weeks_ago = today - datetime.timedelta(days=21)
	four_weeks_ago = today - datetime.timedelta(days=28)
	
	weekly = {}
	weekly['week'] = "Week 1"
	weekly['amount'] = 0
	data.append(weekly)
	
	weekly = {}
	weekly['week'] = "Week 2"
	weekly['amount'] = 0
	data.append(weekly)
	
	weekly = {}
	weekly['week'] = "Week 3"
	weekly['amount'] = 0
	data.append(weekly)
	
	weekly = {}
	weekly['week'] = "Week 4"
	weekly['amount'] = 0
	data.append(weekly)
	
	
	for ticket in mytickets:
		if ticket.closed_on == None:
			continue
			
		ticketdate = ticket.closed_on.date()
		
		if (ticketdate <= today and ticketdate > one_week_ago):
			for i in data:
				if i['week'] == 'Week 4':
					i['amount'] = i['amount'] + 1
			
		elif (ticketdate <= one_week_ago and ticketdate > two_weeks_ago):
			for i in data:
				if i['week'] == 'Week 3':
					i['amount'] = i['amount'] + 1
		elif (ticketdate <= two_weeks_ago and ticketdate > three_weeks_ago):
			for i in data:
				if i['week'] == 'Week 2':
					i['amount'] = i['amount'] + 1
		elif (ticketdate <= three_weeks_ago and ticketdate > four_weeks_ago):
			for i in data:
				if i['week'] == 'Week 1':
					i['amount'] = i['amount'] + 1
					
	return JsonResponse(data, safe=False)
	

	
def monthly(request):
	data = []
	mytickets = Ticket.objects.all()
	today = datetime.date.today()
	
	
	monthly = {}
	monthly['month'] = "Jan"
	monthly['amount'] = 0
	data.append(monthly)
	
		
	monthly = {}
	monthly['month'] = "Feb"
	monthly['amount'] = 0
	data.append(monthly)
		
	monthly = {}
	monthly['month'] = "Mar"
	monthly['amount'] = 0
	data.append(monthly)
		
	monthly = {}
	monthly['month'] = "Apr"
	monthly['amount'] = 0
	data.append(monthly)
	
	monthly = {}
	monthly['month'] = "May"
	monthly['amount'] = 0
	data.append(monthly)
	
	monthly = {}
	monthly['month'] = "Jun"
	monthly['amount'] = 0
	data.append(monthly)
		
	monthly = {}
	monthly['month'] = "Jul"
	monthly['amount'] = 0
	data.append(monthly)
		
	monthly = {}
	monthly['month'] = "Aug"
	monthly['amount'] = 0
	data.append(monthly)
		
	monthly = {}
	monthly['month'] = "Sep"
	monthly['amount'] = 0
	data.append(monthly)
		
	monthly = {}
	monthly['month'] = "Oct"
	monthly['amount'] = 0
	data.append(monthly)
		
	monthly = {}
	monthly['month'] = "Nov"
	monthly['amount'] = 0
	data.append(monthly)
		
	monthly = {}
	monthly['month'] = "Dec"
	monthly['amount'] = 0
	data.append(monthly)
		
	for ticket in mytickets:
		if ticket.closed_on == None:
			continue
			
		ticketdate = ticket.closed_on.date()
		
		for i in data:
			if i['month'] == ticketdate.strftime("%b"):
				i['amount'] = i['amount'] + 1
	
	return JsonResponse(data, safe=False)
	
	