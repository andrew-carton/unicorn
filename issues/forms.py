from django import forms
from .models import Ticket, Comment

	
class TicketForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = ('title', 'description', 'type', 'status', 'feature', 'created_by', 'created_on', 'closed', 'closed_by', 'closed_on')

class TicketFormEdit(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = ('title', 'description', 'type', 'status', 'closed', 'closed_by', 'closed_on')
		
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('ticket', 'comment', 'created_by')
