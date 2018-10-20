from django.conf.urls import url
from .views import tickets, create_ticket, create_comment, edit_ticket

urlpatterns = [
    url(r'^$', tickets, name='tickets'),
	url(r'^ticketform$', create_ticket, name='create_ticket'),
	url(r'^(?P<pk>\d+)/edit/$', edit_ticket, name='edit_ticket'),
	url(r'^commentform$', create_comment, name='create_comment') 
]