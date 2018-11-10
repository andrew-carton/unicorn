from django.conf.urls import url
from .views import bugs, create_ticket, create_comment, edit_ticket, vote, bug, features, feature

urlpatterns = [
	url(r'^bugs$', bugs, name='bugs'),
	url(r'^features$', features, name='features'),
	url(r'^createticket$', create_ticket, name='create_ticket'),
	url(r'^(?P<pk>\d+)/edit/$', edit_ticket, name='edit_ticket'),
	url(r'^(?P<pk>\d+)/bug/$', bug, name='bug'),
	url(r'^(?P<pk>\d+)/feature/$', feature, name='feature'),
	url(r'^comment$', create_comment, name='create_comment'),
	url(r'^(?P<pk>\d+)/vote/$', vote, name='vote') 
]