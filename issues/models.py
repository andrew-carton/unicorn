from django.db import models
from django.utils import timezone

TYPE_PRIORITY = (
	('HIGH', 'HIGH'),
	('MEDIUM', 'MEDIUM'),
	('LOW', 'LOW'),
)

STATUS = (
	('TODO', 'TODO'),
	('DOING', 'DOING'),
	('DONE', 'DONE'),
)

ISSUES = (
	('BUG', 'BUG'),
	('FEATURE', 'FEATURE'),
)

class Ticket(models.Model):
	HIGH = 'HIGH'
	MEDIUM = 'MEDIUM'
	LOW = 'LOW'
	TODO = 'TODO'
	DOING = 'DOING'
	DONE = 'DONE'
	BUG = 'BUG'
	FEATURE = 'FEATURE'
	
	title = models.CharField(max_length=200)
	description = models.TextField()
	type = models.CharField(max_length=6, choices=TYPE_PRIORITY, default=LOW)
	status = models.CharField(max_length=5, choices=STATUS, default=TODO)
	feature = models.CharField(max_length=7, choices=ISSUES, default=BUG)
	votes = models.IntegerField(default=0)
	created_by = models.CharField(max_length=64)
	created_on = models.DateTimeField(auto_now_add=True)
	closed = models.BooleanField(default=False)
	closed_by = models.CharField(max_length=64, blank=True, null=True)
	closed_on = models.DateTimeField(blank=True, null=True)
	
	def __str__(self):
		return self.title

	

