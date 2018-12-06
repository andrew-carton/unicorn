from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Priority types
TYPE_PRIORITY = (
    ('HIGH', 'HIGH'),
    ('MEDIUM', 'MEDIUM'),
    ('LOW', 'LOW'),
)

# Status types
STATUS = (
    ('TODO', 'TODO'),
    ('DOING', 'DOING'),
    ('DONE', 'DONE'),
)

# Issues type
ISSUES = (
    ('BUG', 'BUG'),
    ('FEATURE', 'FEATURE'),
)

"""

	Ticket class- contains the types for a ticket
"""


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
    created_on = models.DateTimeField(default=timezone.now)
    closed = models.BooleanField(default=False)
    closed_by = models.CharField(max_length=64, blank=True, null=True)
    closed_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


"""
	The comment class
"""


class Comment(models.Model):
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    comment = models.TextField()
    created_by = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


"""
	The Vote class - ticket and user as foreign keys to determine
	who has voted
"""


class Vote(models.Model):
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
