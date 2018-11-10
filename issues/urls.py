from django.conf.urls import url
from .views import bugs, create_ticket, create_comment, edit_ticket, vote, bug

urlpatterns = [
    url(r'^$', bugs, name='bugs'),
	url(r'^ticketform$', create_ticket, name='create_ticket'),
	url(r'^(?P<pk>\d+)/edit/$', edit_ticket, name='edit_ticket'),
	url(r'^(?P<pk>\d+)/bug/$', bug, name='bug'),
	url(r'^comment$', create_comment, name='create_comment'),
	url(r'^(?P<pk>\d+)/vote/$', vote, name='vote') 
]