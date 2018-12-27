from django import forms
from .models import Ticket, Comment


"""
	Ticket Form 
"""
class TicketForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = ('title', 'description', 'type', 'status', 'feature', 'created_by', 'created_on', 'closed', 'closed_by', 'closed_on')

	def clean(self):
		cleaned_data = super(TicketForm, self).clean()
		createdon = cleaned_data.get("created_on")
		if not createdon:
			raise forms.ValidationError("Format your date-time like 2018-12-25")

		return cleaned_data


			

"""
	Ticket Form Edit Box

	-- validation checks for status 
"""
class TicketFormEdit(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = ('title', 'description', 'type', 'status', 'closed', 'closed_by', 'closed_on')

	def clean(self):
		data = self.cleaned_data
	
		if data['status'] == Ticket.DONE and data['closed'] == False:
			raise forms.ValidationError(u"Status is DONE also needs to be closed")
		if data['status'] == Ticket.DONE and data['closed_on'] == None:
			raise forms.ValidationError(u"Status DONE also needs a closing date")
		if data['status'] == Ticket.DONE and data['closed_by'] == None:
			raise forms.ValidationError(u"Status DONE also needs a closed by")

		return data
		
