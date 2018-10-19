from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from accounts.views import logout, login, registration


urlpatterns = [
	url(r'^logout/$', logout, name="logout"),
	url(r'^login/$', login, name="login"),
	url(r'^register/$', registration, name="registration"),
]
