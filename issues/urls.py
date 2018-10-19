from django.conf.urls import url
from .views import tickets, create_or_edit_ticket

urlpatterns = [
    url(r'^$', tickets, name='tickets'),
	url(r'^ticketform$', create_or_edit_ticket, name='create_or_edit_ticket'),
	url(r'^(?P<pk>\d+)/edit/$', create_or_edit_ticket, name='edit_ticket') 
]