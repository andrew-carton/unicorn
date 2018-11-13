from django.conf.urls import url
from .views import graphs, progress, daily, weekly, monthly

urlpatterns = [
	url(r'^$', graphs, name='graphs'),
	url(r'^progressstats$', progress, name='progress'),
	url(r'^dailystats$', daily, name='daily'),
	url(r'^weeklystats$', weekly, name='weekly'),
	url(r'^monthlystats$', monthly, name='monthly'),
	]