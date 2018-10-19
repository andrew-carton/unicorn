from django import forms
from .models import Ticket

	
class TicketForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = ('title', 'description', 'type', 'status', 'feature', 'created_by', 'closed', 'closed_by', 'closed_on')
		